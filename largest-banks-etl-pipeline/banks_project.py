# Importing the required libraries
from email import policy
from email.parser import BytesParser
from urllib import response

import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import sqlite3
from datetime import datetime
import re



# TASK 1: LOGGING FUNCTION

def log_progress(message):
    '''This function logs the progress of the code execution
    to a log file.'''

    timestamp_format = '%Y-%h-%d-%H:%M:%S'

    now = datetime.now()

    timestamp = now.strftime(timestamp_format)

    with open('./code_log.txt', 'a') as f:
        f.write(timestamp + ' : ' + message + '\n')

# TASK 2: EXTRACTION FUNCTION

from email import policy
from email.parser import BytesParser

def extract(url, table_attribs):
    '''Extracts information about the top 10 largest banks
    from the saved webpage.'''

    # Read the saved MHTML file
    with open('largest_banks.mhtml', 'rb') as f:
        msg = BytesParser(policy=policy.default).parse(f)

    # Extract HTML content
    page = None

    for part in msg.walk():
        if part.get_content_type() == 'text/html':
            page = part.get_content()
            break

    if page is None:
        raise ValueError("HTML content not found")

    data = BeautifulSoup(page, 'html.parser')

    # Find all table bodies
    tables = data.find_all('tbody')

    if len(tables) < 2:
        raise ValueError("Required bank table not found")

    # Select the correct table containing 10 banks
    rows = tables[1].find_all('tr')

    bank_data = []

    for row in rows:

        col = row.find_all('td')

        if len(col) >= 3:

            bank_name = col[1].get_text(" ", strip=True)

            market_cap = col[2].get_text(strip=True)
            market_cap = market_cap.replace(',', '')
            market_cap = market_cap.rstrip('B')

            bank_data.append({
                "Name": bank_name,
                "MC_USD_Billion": float(market_cap)
            })

    df = pd.DataFrame(bank_data, columns=table_attribs)

    return df

# TASK 3: TRANSFORMATION FUNCTION

def transform(df, csv_path):
    '''This function converts the market capitalization
    from USD into GBP, EUR and INR.'''

    exchange_rate = pd.read_csv(csv_path)

    exchange_rate = dict(
        zip(
            exchange_rate.iloc[:, 0],
            exchange_rate.iloc[:, 1]
        )
    )

    # Convert exchange rates into float

    exchange_rate = {
        currency: float(rate)
        for currency, rate in exchange_rate.items()
    }

    # Convert USD into GBP

    gbp_rate = float(exchange_rate['GBP'])

    df['MC_GBP_Billion'] = [
        np.round(x * gbp_rate, 2)
        for x in df['MC_USD_Billion']
    ]

    # Convert USD into EUR

    eur_rate = float(exchange_rate['EUR'])

    df['MC_EUR_Billion'] = [
        np.round(x * eur_rate, 2)
        for x in df['MC_USD_Billion']
    ]

    # Convert USD into INR

    inr_rate = float(exchange_rate['INR'])

    df['MC_INR_Billion'] = [
        np.round(x * inr_rate, 2)
        for x in df['MC_USD_Billion']
    ]

    return df


# TASK 4: LOAD DATA INTO CSV

def load_to_csv(df, output_path):
    '''This function saves the transformed DataFrame
    into a CSV file.'''

    df.to_csv(output_path, index=False)


# TASK 5: LOAD DATA INTO DATABASE

def load_to_db(df, sql_connection, table_name):
    '''This function saves the transformed DataFrame
    into an SQLite database table.'''

    df.to_sql(
        table_name,
        sql_connection,
        if_exists='replace',
        index=False
    )


# TASK 6: RUN SQL QUERIES

def run_queries(query_statement, sql_connection):
    '''This function executes SQL queries and
    displays the query output.'''

    print(query_statement)

    query_output = pd.read_sql(query_statement, sql_connection)

    print(query_output)


# MAIN ETL EXECUTION


# Declaring known values

url = 'https://web.archive.org/web/20230908091635/https://en.wikipedia.org/wiki/List_of_largest_banks'

table_attribs = ['Name', 'MC_USD_Billion']

csv_path = './exchange_rate.csv'

output_path = './largest_banks_data.csv'
table_name = 'Largest_banks'


# Log the beginning of the ETL process

log_progress('Preliminaries complete. Initiating ETL process')


# EXTRACTION

df = extract(url, table_attribs)
print("Extracted Data:")
print(df)

print("Number of banks extracted:", len(df))

log_progress('Data extraction complete. Initiating Transformation process')


# TRANSFORMATION

df = transform(df, csv_path)

log_progress('Data transformation complete. Initiating Loading process')

# Print the fifth bank's market capitalization in EUR

print(df['MC_EUR_Billion'][4])


# LOAD TO CSV

load_to_csv(df, output_path)

log_progress('Data saved to CSV file')


# CREATE SQLITE DATABASE CONNECTION

sql_connection = sqlite3.connect('Banks.db')

log_progress('SQL Connection initiated')


# LOAD DATA INTO DATABASE

load_to_db(df, sql_connection, table_name)

log_progress('Data loaded to Database as a table, Executing queries')


# QUERY 1: DISPLAY THE ENTIRE TABLE

query_statement = 'SELECT * FROM Largest_banks'

run_queries(query_statement, sql_connection)


# QUERY 2: FIND AVERAGE MARKET CAPITALIZATION IN GBP

query_statement = 'SELECT AVG(MC_GBP_Billion) FROM Largest_banks'

run_queries(query_statement, sql_connection)


# QUERY 3: DISPLAY THE TOP 5 BANK NAMES

query_statement = 'SELECT Name FROM Largest_banks LIMIT 5'

run_queries(query_statement, sql_connection)


# LOG PROCESS COMPLETION

log_progress('Process Complete')


# CLOSE DATABASE CONNECTION

sql_connection.close()

log_progress('Server Connection closed')