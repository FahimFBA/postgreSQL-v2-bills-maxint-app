# Implementation Details for Recurring Transaction Identification

Based on the analysis of transaction patterns and data characteristics, the following methodologies were used to identify recurring transactions.

## Implementation Details

### 1. Scoring System
We implemented a weighted scoring system based on multiple factors:
- Time interval regularity (weight: 0.3)
- Amount consistency (weight: 0.25)
- Description match (weight: 0.25) (always 1 in the current implementation)
- Transaction type match (weight: 0.1)
- Category match (weight: 0.1)

The system uses a threshold of 0.4 to identify recurring transactions, balancing between sensitivity and specificity.

### 2. Major Functions

#### `calculate_score(group)`
This function calculates the score for a group of transactions with the same description. It considers:
- Time interval regularity
- Amount consistency
- Transaction type match
- Category match

#### `identify_recurring_transactions(df)`
This function applies the scoring system to identify recurring transactions. It:
- Groups transactions by description
- Applies the `calculate_score` function to each group
- Filters transactions with a score above 0.4 and at least 2 occurrences

#### `predict_next_date(dates)`
This function predicts the next occurrence of a recurring transaction by:
- Calculating the average interval between transactions
- Adding this interval to the last known transaction date

### 3. Process Flow
1. Load and preprocess the transaction data
2. Group transactions by description
3. Calculate scores for each group, including detailed debugging information
4. Filter recurring transactions based on score (> 0.4) and frequency (>= 2 occurrences)
5. Predict the next occurrence date for each recurring transaction
6. Apply a maximum future date limit (10 years from current date) for predicted next dates
7. Sort the recurring transactions by next predicted date
8. Generate a new CSV with identified recurring transactions

## Challenges Addressed

1. **Variable Amounts**: The scoring system allows for some variation in amounts while still identifying recurring transactions.

2. **Irregular Intervals**: By using an average interval, the system can handle some irregularity in transaction timing.

3. **New Recurring Transactions**: The system requires at least two occurrences, balancing between identifying new patterns and avoiding false positives.

4. **Discontinued Transactions**: The next date prediction always ensures future dates, implicitly handling discontinued transactions.

## Future Improvements

1. Implement a more sophisticated time series analysis for better handling of irregular intervals.
2. Incorporate machine learning models for improved pattern recognition.
3. Develop a feedback mechanism to continuously improve the identification accuracy based on user input.
4. Implement more granular category matching to improve accuracy in specific transaction types.
5. Fine-tune the scoring weights and threshold based on real-world performance data.
6. Enhance the debugging and logging capabilities for better transparency and troubleshooting.
7. Implement adaptive time interval prediction for more accurate next date estimates.

## Validation Process

To ensure the accuracy of the recurring transaction identification:
1. Manually review a sample of identified recurring transactions.
2. Compare the results with known recurring bills from a subset of accounts.
3. Analyze false positives and false negatives to refine the scoring system.
4. Periodically update the identification criteria based on new patterns observed in the data.
