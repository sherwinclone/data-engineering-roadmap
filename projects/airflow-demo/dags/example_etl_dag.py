"""
Example ETL DAG 範例 ETL DAG

A simple DAG demonstrating extract → transform → load flow.
示範 extract → transform → load 流程的簡單 DAG。
"""

from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.python import PythonOperator

default_args = {
    "owner": "data-eng",
    "retries": 2,
    "retry_delay": timedelta(minutes=5),
}


def extract(**kwargs):
    print("Extracting data...")
    return {"row_count": 100}


def transform(**kwargs):
    ti = kwargs["ti"]
    result = ti.xcom_pull(task_ids="extract")
    print(f"Transforming {result['row_count']} rows...")
    return {"row_count": result["row_count"]}


def load(**kwargs):
    ti = kwargs["ti"]
    result = ti.xcom_pull(task_ids="transform")
    print(f"Loading {result['row_count']} rows...")


with DAG(
    dag_id="example_etl",
    default_args=default_args,
    description="A simple ETL DAG 簡單 ETL DAG",
    schedule="@daily",
    start_date=datetime(2024, 1, 1),
    catchup=False,
) as dag:
    t_extract = PythonOperator(task_id="extract", python_callable=extract)
    t_transform = PythonOperator(task_id="transform", python_callable=transform)
    t_load = PythonOperator(task_id="load", python_callable=load)

    t_extract >> t_transform >> t_load
