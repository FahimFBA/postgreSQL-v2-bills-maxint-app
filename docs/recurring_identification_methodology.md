# Methodologies for Identifying Recurring Transactions

Based on the analysis of transaction patterns and data characteristics, the following methodologies can be used to identify recurring transactions.

## Key Identification Methods

### 1. Pattern-based Identification
- Match transactions with identical `description` and `amount` combinations
- Track transactions from the same `counterParty`
- Examples of known recurring patterns:
  - Phone bills (AT&T)
  - Credit card payments (American Express)
  - Automated savings transfers

### 2. Time-based Analysis
- Analyze regular intervals between transactions
- Common intervals to check:
  - Monthly (most common for bills)
  - Bi-weekly (common for transfers)
  - Weekly (subscriptions)
- Calculate the average time delta between similar transactions

### 3. Transaction Type Indicators
Priority transaction types that suggest recurring nature:
- `phone`
- `bill_payment`
- `transfer` (with "Recurring" in description)
- `ach` (automated clearing house)

### 4. Category Analysis
Categories more likely to contain recurring transactions:
- `utilities`
- `service`
- `software`
- `general` (when combined with recurring transfer patterns)

### 5. Scoring System
Weighted scoring based on multiple factors:
- Payment interval regularity (weight: 0.3)
- Amount consistency (weight: 0.25)
- Description/counterParty match (weight: 0.25)
- Transaction type match (weight: 0.1)
- Category match (weight: 0.1)

## Implementation Guidelines

1. **Primary Indicators**
   - Regular time intervals
   - Consistent amounts
   - Matching descriptions

2. **Secondary Indicators**
   - Transaction type
   - Category
   - CounterParty

3. **Minimum Criteria**
   A transaction should be flagged as recurring if:
   - It appears at least twice with the same amount and description
   - Shows a regular time interval pattern
   - Belongs to a typical recurring category

## Edge Cases to Consider

1. **Variable Amounts**
   - Utility bills that change monthly
   - Subscription services with usage-based pricing

2. **Irregular Intervals**
   - Quarterly payments
   - Annual subscriptions
   - Bi-monthly services

3. **New Recurring Transactions**
   - Recently started subscriptions
   - New bill payments

4. **Discontinued Recurring Transactions**
   - Cancelled subscriptions
   - Completed loan payments

## Validation Process

1. Check for false positives by:
   - Verifying consistency over time
   - Confirming with transaction type indicators
   - Validating against known recurring payees

2. Monitor accuracy by:
   - Tracking prediction success rate
   - Adjusting weights based on performance
   - Regular review of edge cases