# file_upload.py
import pandas as pd
import psycopg2

def load_data():
    # Database connection parameters
    host = 'localhost'
    port = '5432'
    dbname = 'telecommunication'
    user = 'postgres'
    password = 'aym'  # replace with your actual password

    # Establishing the connection
    connection = psycopg2.connect(
        host=host,
        port=port,
        dbname=dbname,
        user=user,
        password=password
    )

    # Query to select all data from xdr_data
    query = 'SELECT * FROM xdr_data;'

    # Importing the data into a pandas DataFrame
    xdr_data_df = pd.read_sql_query(query, connection)

    # Closing the connection
    connection.close()
    
    return xdr_data_df  # Return the DataFrame
# Load the data from the database
xdr_data_df = load_data()

# Print the first 5 rows of the DataFrame
print(xdr_data_df.head())