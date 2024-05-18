from datetime import timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago
from datetime import datetime
from twitter_etl import run_twitter_etl

default_args = {
    'owner': 'Meet',
    'depends_on_past': False,
    'start_date': datetime(2024, 22, 1),
    'email': ['imeetpatel47@gamil.com'],
    'email_on_failure': True,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1)
}

dag = DAG(
    'twitter_dag',
    default_args=default_args,
    description='imVkohli_twitter_etl!',
    schedule_interval=timedelta(days=1),
)

run_etl = PythonOperator(
    task_id='task_1_twitter_etl',
    python_callable=run_twitter_etl,
    dag=dag, 
)

run_etl
