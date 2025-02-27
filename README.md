# PostgreSQL V2 Bills Maxint App

## Tasks/Goals
The entire goals of this project is located in the [tasks](./tasks/) directory.

## Step by Step Approach to the Solution

### Analysis of the Database
The database is a CSV file containing bank transaction data with columns: id, createdAt, externalId, type, amount, date, description, category, counterParty, recurring, tag, accountExternalId, and location.

| Parameter | Description |
| --- | --- |
| id | The unique identifier for the transaction. |
| createdAt | The timestamp when the transaction was created. |
| externalId | The external identifier for the transaction. |
| type | The type of transaction (e.g., card_payment, digital_payment). |
| amount | The amount of the transaction. |
| date | The date of the transaction. |
| description | The description of the transaction. |
| category | The category of the transaction. |
| counterParty | The counterparty involved in the transaction. |
| recurring | A flag indicating whether the transaction is recurring. |
| tag | A tag associated with the transaction. |
| accountExternalId | The external identifier for the account. |
| location | The location of the transaction. |
