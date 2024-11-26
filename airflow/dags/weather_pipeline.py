from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import sys
import os

# Add src directory to Python path
sys.path.append(os.path.join(os.environ['AIRFLOW_HOME'], '..', 'src'))

from collect_data import collect_weather_data
from preprocess_data import preprocess_data
from train_model import train_model

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 1, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'weather_pipeline',
    default_args=default_args,
    description='Weather data pipeline',
    schedule_interval=timedelta(days=1),
)

collect_task = PythonOperator(
    task_id='collect_data',
    python_callable=collect_weather_data,
    dag=dag,
)

preprocess_task = PythonOperator(
    task_id='preprocess_data',
    python_callable=preprocess_data,
    dag=dag,
)

train_task = PythonOperator(
    task_id='train_model',
    python_callable=train_model,
    dag=dag,
)

collect_task >> preprocess_task >> train_task