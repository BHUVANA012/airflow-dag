import datetime
from airflow import DAG
from airflow.operators.python_operator import PythonOperator

def print_hello():
    print("Hello, Airflow!")

dag = DAG('hello_world', description='Hello World DAG',
          schedule_interval='0 12 * * *',
          start_date=datetime.datetime(2022, 8, 24),
          catchup=False)

hello_operator = PythonOperator(task_id='hello_task', python_callable=print_hello, dag=dag)
