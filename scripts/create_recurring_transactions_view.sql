-- Drop the existing table if it exists
DROP TABLE IF EXISTS recurring_transactions;

-- Create the table for recurring transactions
CREATE TABLE recurring_transactions (
    id SERIAL PRIMARY KEY,
    amount NUMERIC,
    description TEXT,
    next_date TIMESTAMP,
    last_date DATE,
    first_date DATE
);

-- Create the view for recurring transactions
CREATE OR REPLACE VIEW recurring_transactions_view AS
SELECT
    amount,
    description,
    next_date,
    last_date,
    first_date
FROM
    recurring_transactions
ORDER BY
    next_date ASC;

-- Grant access to the authenticated role
GRANT SELECT, INSERT, UPDATE ON recurring_transactions TO authenticated;
GRANT SELECT ON recurring_transactions_view TO authenticated;
GRANT USAGE, SELECT ON SEQUENCE recurring_transactions_id_seq TO authenticated;

-- Example query to test the view
-- SELECT * FROM recurring_transactions_view LIMIT 5;
