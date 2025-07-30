from datetime import datetime, timedelta
import logging
from pathlib import Path

from airflow import DAG  # type: ignore
from airflow.operators.bash import BashOperator  # type: ignore
from airflow.utils.dates import days_ago  # type: ignore

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

default_args = {
    "start_date": days_ago(1),
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=2),
    "catchup": False,
}

dag = DAG(
    "staging_dag",
    default_args=default_args,
    description="dbt staging pipeline",
    schedule_interval=timedelta(days=1),
    max_active_runs=1
)

# dbt project paths (in container)
DBT_PROJECT_DIR = "/opt/airflow/dbt/marvan_covid"
DBT_PROFILES_DIR = "/opt/airflow/dbt/marvan_covid"

dbt_debug = BashOperator(
    task_id="dbt_debug",
    bash_command=f"cd {DBT_PROJECT_DIR} && dbt debug --profiles-dir {DBT_PROFILES_DIR}",
    dag=dag,
)

dbt_test_staging = BashOperator(
    task_id="dbt_test_staging",
    bash_command=f"cd {DBT_PROJECT_DIR} && dbt test --select path:models/staged --profiles-dir {DBT_PROFILES_DIR}",
    dag=dag,
)

dbt_run_staging = BashOperator(
    task_id="dbt_run_staging",
    bash_command=f"cd {DBT_PROJECT_DIR} && dbt run --select path:models/staged --profiles-dir {DBT_PROFILES_DIR}",
    dag=dag,
)


dbt_debug >> dbt_test_staging >> dbt_run_staging 