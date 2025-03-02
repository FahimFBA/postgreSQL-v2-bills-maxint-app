import os
import pandas as pd
from dotenv import load_dotenv
from supabase import create_client, Client
import json

# Load environment variables
load_dotenv()

# Initialize Supabase client
url: str = os.environ.get("SUPABASE_URL", "")
key: str = os.environ.get("SUPABASE_KEY", "")

if not url or not key:
    raise ValueError("SUPABASE_URL and SUPABASE_KEY must be set in the .env file")

supabase: Client = create_client(url, key)

def test_supabase_connection():
    try:
        # Try to fetch the list of tables
        result = supabase.table('').select('*').limit(1).execute()
        print("Supabase connection test successful")
        print(f"Result: {json.dumps(result.data, indent=2)}")
    except Exception as e:
        print("Supabase connection test failed")
        print(f"Error details: {str(e)}")
        print(f"Full error object: {e}")

def upload_to_supabase(file_path: str, table_name: str):
    try:
        # Read the CSV file
        df = pd.read_csv(file_path, parse_dates=['next_date', 'last_date', 'first_date'])
        
        print(f"Loaded {len(df)} rows from {file_path}")
        print("Sample data:")
        print(df.head())
        
        # Convert DataFrame to list of dictionaries
        data = df.to_dict('records')
        
        # Convert datetime objects to ISO format strings
        for row in data:
            row['next_date'] = row['next_date'].isoformat()
            row['last_date'] = row['last_date'].isoformat()
            row['first_date'] = row['first_date'].isoformat()
        
        # Upload data to Supabase in batches
        batch_size = 100
        for i in range(0, len(data), batch_size):
            batch = data[i:i+batch_size]
            result = supabase.table(table_name).upsert(batch).execute()
            print(f"Uploaded batch {i//batch_size + 1} of {len(data)//batch_size + 1}")
        
        print(f"Successfully uploaded {len(data)} rows to {table_name}")
    except Exception as e:
        print(f"An error occurred while uploading data to {table_name}")
        print(f"Error details: {str(e)}")
        print(f"Full error object: {e}")
        raise

if __name__ == "__main__":
    print("Testing Supabase connection...")
    test_supabase_connection()
    
    print("\nUploading data to Supabase...")
    input_file = "tasks/recurring_transactions.csv"
    table_name = "recurring_transactions"
    upload_to_supabase(input_file, table_name)

print("""
Before running this script, please ensure that the table is created in Supabase using the SQL provided in the 'scripts/create_recurring_transactions_view.sql' file.
""")
