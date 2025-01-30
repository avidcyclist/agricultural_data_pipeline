from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
from data_ingestion.fetch_crop_yield_data import fetch_crop_yield_data
from etl.data_cleaning import clean_crop_yield_data
from etl.data_transformation import transform_crop_yield_data
from etl.load_to_postgres import load_crop_yield_data_to_postgres

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 1, 1),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'crop_yield_etl_dag',
    default_args=default_args,
    description='A DAG for ETL process of crop yield data',
    schedule_interval='@daily',
)

fetch_data = PythonOperator(
    task_id='fetch_crop_yield_data',
    python_callable=fetch_crop_yield_data,
    dag=dag,
)

clean_data = PythonOperator(
    task_id='clean_crop_yield_data',
    python_callable=clean_crop_yield_data,
    dag=dag,
)

transform_data = PythonOperator(
    task_id='transform_crop_yield_data',
    python_callable=transform_crop_yield_data,
    dag=dag,
)

load_data = PythonOperator(
    task_id='load_crop_yield_data_to_postgres',
    python_callable=load_crop_yield_data_to_postgres,
    dag=dag,
)

fetch_data >> clean_data >> transform_data >> load_data