import os
import sys
from airflow.utils.dates import days_ago
from airflow.operators.python import PythonOperator
from airflow import DAG
from datetime import timedelta

current_path = os.path.dirname(os.path.abspath(__file__))
parent_path = os.path.abspath(os.path.join(current_path, '..', '..'))
sys.path.append(parent_path)
from src.logger import setup_logging
from src.data_loader.api_ingestion import main as api_ingestion
from src.minio_to_snowflake import minio_raw_data_to_snowflake

def _run_api_ingestion(**kwargs):
    """Airflow callable to run API ingestion and log progress."""
    ti = kwargs['ti']
    ti.log.info("Starting API ingestion task")
    try:
        result = api_ingestion()
        ti.log.info(f"API ingestion completed: {result}")
        return result
    except Exception as e:
        ti.log.error(f"API ingestion failed: {e}")
        raise

def _run_minio_to_snowflake(**kwargs):
    """Airflow callable to load data from MinIO to Snowflake and log progress."""
    ti = kwargs['ti']
    ti.log.info("Starting MinIO to Snowflake ingestion task")
    try:
        result = minio_raw_data_to_snowflake()
        ti.log.info(f"MinIO to Snowflake ingestion completed: {result}")
        return result
    except Exception as e:
        ti.log.error(f"MinIO to Snowflake ingestion failed: {e}")
        raise

with DAG(
    dag_id="ingestion_dag",
    description="Raw data ingestion pipeline - runs every day",
    schedule_interval=timedelta(days=1),
    start_date=days_ago(1),
    catchup=False,
) as dag:

    api_ingestion_task = PythonOperator(
        task_id="api_ingestion",
        python_callable=_run_api_ingestion,
        provide_context=True
    )

    minio_to_snowflake_task = PythonOperator(
        task_id="minio_to_snowflake_ingestion",
        python_callable=_run_minio_to_snowflake,
        provide_context=True
    )

    api_ingestion_task >> minio_to_snowflake_task
