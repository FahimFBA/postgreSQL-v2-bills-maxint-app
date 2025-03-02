-- Query the original table
SELECT 'Original Table' AS source, *
FROM recurring_transactions
LIMIT 5;

-- Query the view
SELECT 'View' AS source, *
FROM recurring_transactions_view
LIMIT 5;

-- Compare column names and ordering
SELECT 'recurring_transactions' AS table_name, column_name, data_type, ordinal_position
FROM information_schema.columns
WHERE table_name = 'recurring_transactions'
UNION ALL
SELECT 'recurring_transactions_view' AS table_name, column_name, data_type, ordinal_position
FROM information_schema.columns
WHERE table_name = 'recurring_transactions_view'
ORDER BY table_name, ordinal_position;
