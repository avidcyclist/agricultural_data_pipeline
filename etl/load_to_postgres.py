import psycopg2
import pandas as pd

def load_data_to_postgres(dataframe, table_name, db_config):
    """
    Load a DataFrame to a PostgreSQL table.

    Parameters:
    - dataframe: The DataFrame to load.
    - table_name: The name of the table to load data into.
    - db_config: A dictionary containing database connection parameters.
    """
    try:
        # Establish a connection to the PostgreSQL database
        conn = psycopg2.connect(
            dbname=db_config['dbname'],
            user=db_config['user'],
            password=db_config['password'],
            host=db_config['host'],
            port=db_config['port']
        )
        cursor = conn.cursor()

        # Load the DataFrame into the PostgreSQL table
        dataframe.to_sql(table_name, conn, if_exists='replace', index=False)

        # Commit the transaction
        conn.commit()
        print(f"Data loaded successfully into {table_name}.")

    except Exception as e:
        print(f"Error loading data to PostgreSQL: {e}")

    finally:
        # Close the database connection
        cursor.close()
        conn.close()

# Example usage
if __name__ == "__main__":
    # Sample DataFrame
    df = pd.DataFrame({
        'column1': [1, 2, 3],
        'column2': ['A', 'B', 'C']
    })

    # Database configuration
    db_config = {
        'dbname': 'your_db_name',
        'user': 'your_username',
        'password': 'your_password',
        'host': 'localhost',
        'port': '5432'
    }

    load_data_to_postgres(df, 'your_table_name', db_config)