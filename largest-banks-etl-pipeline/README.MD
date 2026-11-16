# Largest Banks ETL Pipeline

## Project Overview
This project extracts information about the world's largest banks by market capitalization from an archived Wikipedia page, transforms their market capitalization values into GBP, EUR, and INR, and loads the processed data into a CSV file and an SQLite database.

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
- Retrieve the largest banks table from an archived Wikipedia page.
- Extract the bank names and market capitalization values in USD.
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
- Load the data into an SQLite database named `Banks.db`.
- Store the data in a table named `Largest_banks`.

## SQL Queries
The project executes the following queries:

1. Retrieve all records from the `Largest_banks` table.
2. Calculate the average market capitalization in GBP.
3. Retrieve the names of the first five banks.

## Project Files

| File | Description |
|---|---|
| `banks_project.py` | Main ETL Python script |
| `exchange_rate.csv` | Currency exchange rates |
| `largest_banks_data.csv` | Transformed output data |
| `Banks.db` | SQLite database |
| `code_log.txt` | ETL execution log |
| `requirements.txt` | Python dependencies |

## How to Run

Clone this repository:

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the project:

```bash
python banks_project.py
```

## Results

- Successfully extracted information for 10 banks.
- Converted market capitalization values into three currencies.
- Generated a CSV output file.
- Stored processed data in SQLite.
- Executed SQL queries successfully.

## Learning Outcomes

- Understanding ETL pipelines.
- Web scraping with BeautifulSoup.
- Data transformation using Pandas and NumPy.
- Working with CSV files.
- Database operations using SQLite.
- Executing SQL queries from Python.

## Author
Created as part of the IBM Data Engineering learning journey.