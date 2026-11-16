# Largest Banks ETL Pipeline

## Project Overview

This project implements an ETL (Extract, Transform, Load) pipeline to process information about the world's largest banks by market capitalization.

The pipeline extracts bank names and market capitalization values in USD, transforms the values into GBP, EUR, and INR using exchange rates, and loads the processed data into a CSV file and an SQLite database.

This project was completed as part of the IBM Data Engineering course on Coursera.

## Technologies Used

- Python
- Pandas
- NumPy
- BeautifulSoup
- Requests
- SQLite3
- SQL

## ETL Workflow

### 1. Extract

- Read the archived Wikipedia webpage saved as an MHTML file.
- Extract bank names and market capitalization values in USD.
- Store the extracted information in a Pandas DataFrame.

### 2. Transform

- Read currency exchange rates from `exchange_rate.csv`.
- Convert market capitalization values from USD into:
  - GBP
  - EUR
  - INR
- Round converted values to two decimal places.

### 3. Load

- Export the transformed DataFrame to `largest_banks_data.csv`.
- Load the processed data into an SQLite database named `Banks.db`.
- Store the data in a table named `Largest_banks`.

## SQL Queries

The project executes the following SQL queries:

1. Retrieve all records from the `Largest_banks` table.
2. Calculate the average market capitalization in GBP.
3. Retrieve the names of the first five banks.

## Project Structure

| File | Description |
|---|---|
| `banks_project.py` | Main ETL Python script |
| `exchange_rate.csv` | Currency exchange rates |
| `largest_banks.mhtml` | Archived webpage used as the extraction source |
| `largest_banks_data.csv` | Transformed output data |
| `requirements.txt` | Python dependencies |
| `.gitignore` | Excludes generated and unnecessary files |

## How to Run

### 1. Clone the repository

```bash
git clone https://github.com/Nisarga-61/largest-banks-etl-pipeline.git
```

### 2. Navigate to the project directory

```bash
cd largest-banks-etl-pipeline
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the ETL pipeline

```bash
python banks_project.py
```

## Results

- Successfully extracted information for 10 banks.
- Converted market capitalization values into GBP, EUR, and INR.
- Generated a transformed CSV file.
- Loaded processed data into an SQLite database.
- Successfully executed SQL queries.

## Learning Outcomes

- Understanding ETL pipeline development.
- Web data extraction using BeautifulSoup.
- Data transformation using Pandas and NumPy.
- Reading and writing CSV files.
- Database operations using SQLite.
- Executing SQL queries through Python.

## Author

Created as part of the IBM Data Engineering learning journey.
