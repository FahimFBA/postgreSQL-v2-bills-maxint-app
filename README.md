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

### EDA (Exploratory Data Analysis)
The EDA is done in the [notebooks](./notebooks/) directory.

### Parameter Analysis

#### id

The id parameter is a unique identifier for the transaction. It is a string data type. There is 100 unique values in the id column. It is the representation of the transaction.

![id](./notebooks/id%20Types%20Count.png)

#### createdAt

The createdAt parameter is the timestamp when the transaction was created. There is only 1 unique value in the createdAt column. Therefore, all of the transactions were created at the same time.

![createdAt](./notebooks/createdAt%20Types%20Count.png)

#### externalId

The externalId parameter is the external identifier for the transaction. It is a string data type. There is 100 unique values in the externalId column. It is the representation of the transaction.

![externalId](./notebooks/externalId%20Types%20Count.png)

#### type

The type parameter is the type of transaction (e.g., card_payment, digital_payment). It is a string data type. There are 16 unique values in the type column. 

![type](./notebooks/type%20Types%20Count.png)

The maximum number of transactions is card_payment. The minimum number of transactions is charge.

### amount

The amount parameter is the amount of the transaction. It is a float data type. There are 88 positive values and 12 negative amounts in the amount column.

![amount](./notebooks/amount_distribution.png)

### date

The date parameter is the date of the transaction. It is a string data type. There are 76 unique values in the date column.

![date](./notebooks/date%20Types%20Count.png)


### description

The description parameter is the description of the transaction. It is a string data type. There are 57 unique values in the description column.

![description](./notebooks/description%20Types%20Count.png)

### category

The category parameter is the category of the transaction. It is a string data type. There are 13 unique values in the category column.

![category](./notebooks/category.png)

### counterParty

The counterParty parameter is the counterparty involved in the transaction. It is a string data type. There are 57 unique values in the counterParty column.

![counterParty](./notebooks/counterParty%20Types%20Count.png)

### recurring

The recurring parameter is a flag indicating whether the transaction is recurring. It is a boolean data type. There are 0 unique values in the recurring column.

### tag

The tag parameter is a tag associated with the transaction. It is a string data type. There are 3 unique values in the tag column.

![tag](./notebooks/tag%20Types%20Count.png)

### accountExternalId

The accountExternalId parameter is the external identifier for the account. It is a string data type. There are 3 unique values in the accountExternalId column.

![accountExternalId](./notebooks/accountExternalId%20Types%20Count.png)

### location

The location parameter is the location of the transaction. It is a string data type. There are 3 unique values in the location column.

![location](./notebooks/location%20Types%20Count.png)