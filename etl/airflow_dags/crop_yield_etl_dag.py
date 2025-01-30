from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
from data_ingestion.fetch_crop_yield_data import fetch_crop_yield_data
from data_ingestion.upload_to_s3 import upload_to_s3

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2023, 1, 1),
    'retries': 1,
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

upload_data = PythonOperator(
    task_id='upload_to_s3',
    python_callable=upload_to_s3,
    dag=dag,
)

fetch_data >> upload_data