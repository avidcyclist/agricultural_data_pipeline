import psycopg2
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

def load_data_to_postgres(dataframe, table_name, db_config):
    """
    Load a DataFrame to a PostgreSQL table.

    Parameters:
    - dataframe: The DataFrame to load.
    - table_name: The name of the table to load data into.
    - db_config: A dictionary containing database connection parameters.
    """
    try:
        # Create a SQLAlchemy engine
        engine = create_engine(
            f"postgresql+psycopg2://{db_config['user']}:{db_config['password']}@{db_config['host']}:{db_config['port']}/{db_config['dbname']}"
        )

        # Load the DataFrame into the PostgreSQL table
        dataframe.to_sql(table_name, engine, if_exists='append', index=False)
        print(f"Data loaded successfully into {table_name}.")

    except Exception as e:
        print(f"Error loading data to PostgreSQL: {e}")

# Example usage
if __name__ == "__main__":
    # Sample DataFrame
    df = pd.DataFrame({
        'column1': [1, 2, 3],
        'column2': ['A', 'B', 'C']
    })

    # Database configuration
    db_config = {
        'dbname': os.getenv('DB_NAME'),
        'user': os.getenv('DB_USER'),
        'password': os.getenv('DB_PASSWORD').strip(),
        'host': os.getenv('DB_HOST'),
        'port': os.getenv('DB_PORT')
    }

    # Replace 'your_table_name' with the actual table name
    load_data_to_postgres(df, 'crop_yield_data', db_config)