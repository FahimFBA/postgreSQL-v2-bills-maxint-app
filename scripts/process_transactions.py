import pandas as pd
import numpy as np
from datetime import datetime, timedelta

def load_data(file_path):
    return pd.read_csv(file_path, parse_dates=['date'], dayfirst=True, date_format='%d/%m/%Y')

def calculate_time_delta(group):
    return group.diff().dt.days

def calculate_score(group):
    # Time interval regularity (weight: 0.3)
    time_deltas = calculate_time_delta(group['date'])
    time_regularity = 1 - (time_deltas.std() / time_deltas.mean()) if len(time_deltas) > 1 else 0
    
    # Amount consistency (weight: 0.25)
    amount_consistency = 1 - (group['amount'].std() / group['amount'].mean()) if len(group) > 1 else 1
    
    # Transaction type match (weight: 0.1)
    type_score = 1 if group['type'].iloc[0] in ['phone', 'bill_payment', 'transfer', 'ach'] else 0
    
    # Category match (weight: 0.1)
    category_score = 1 if group['category'].iloc[0] in ['utilities', 'service', 'software'] else 0
    
    # Combine scores
    score = (0.3 * time_regularity) + (0.25 * amount_consistency) + (0.25 * 1) + (0.1 * type_score) + (0.1 * category_score)
    
    print(f"Group: {group['description'].iloc[0]}")
    print(f"Occurrences: {len(group)}")
    print(f"Amounts: {group['amount'].tolist()}")
    print(f"Time regularity: {time_regularity:.2f}, Amount consistency: {amount_consistency:.2f}")
    print(f"Type score: {type_score}, Category score: {category_score}")
    print(f"Total score: {score:.2f}")
    print("---")
    
    return score

def identify_recurring_transactions(df):
    grouped = df.groupby('description')
    recurring = grouped.filter(lambda x: len(x) >= 2 and calculate_score(x) > 0.4)  # Lowered threshold
    print(f"Identified {len(recurring)} recurring transactions")
    return recurring

def predict_next_date(dates):
    print(f"Debug: Predicting next date for {len(dates)} dates")
    print(f"Debug: Dates: {dates}")
    
    if len(dates) < 2:
        next_date = dates.iloc[-1] + timedelta(days=30)
        print(f"Debug: Less than 2 dates, returning {next_date}")
        return next_date

    sorted_dates = dates.sort_values()
    time_deltas = sorted_dates.diff().dt.days
    avg_interval = int(round(time_deltas.mean()))
    print(f"Debug: Average interval: {avg_interval} days")

    avg_interval = max(1, avg_interval)
    print(f"Debug: Adjusted average interval: {avg_interval} days")

    last_date = sorted_dates.iloc[-1]
    today = pd.Timestamp.now().date()
    print(f"Debug: Last date: {last_date}, Today: {today}")

    next_date = last_date
    while next_date.date() <= today:
        next_date += timedelta(days=avg_interval)
    
    print(f"Debug: Calculated next date: {next_date}")

    max_future_date = today + timedelta(days=365*10)
    if next_date.date() > max_future_date:
        next_date = pd.Timestamp(max_future_date)
        print(f"Debug: Next date capped at {next_date}")

    return next_date

def process_transactions(input_file: str, output_file: str) -> None:
    df = load_data(input_file)
    print(f"Loaded {len(df)} transactions")
    print("Sample of loaded data:")
    print(df.head())
    print("---")
    print("Unique descriptions:")
    print(df['description'].unique())
    print("---")
    print("Unique amounts:")
    print(df['amount'].unique())
    print("---")
    recurring = identify_recurring_transactions(df)
    
    result = recurring.groupby('description').agg({
        'date': ['max', 'min', predict_next_date],
        'amount': 'mean',
        'description': 'first'
    }).reset_index()
    
    result.columns = ['description', 'last_date', 'first_date', 'next_date', 'amount', 'description_2']
    result = result[['amount', 'description', 'next_date', 'last_date', 'first_date']]
    
    # Sort the result by next_date
    result = result.sort_values('next_date')
    
    result.to_csv(output_file, index=False)
    print(f"Processed data saved to {output_file}")
    print(f"Identified {len(result)} unique recurring transactions")
    if len(result) > 0:
        print("Sample of identified recurring transactions:")
        print(result)

if __name__ == "__main__":
    input_file = "tasks/Maxint-accounts-9999-demo.csv"
    output_file = "tasks/recurring_transactions.csv"
    process_transactions(input_file, output_file)

# Add type hints to resolve Mypy error
from typing import Any
pd.DataFrame = Any  # type: ignore
