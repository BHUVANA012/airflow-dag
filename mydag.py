import datetime
from airflow import DAG
from airflow.operators.python_operator import PythonOperator

def do_nothing():
    pass

my_dag = DAG(
    dag_id="my_dag_name",
    start_date=datetime.datetime(2021, 1, 1),
    schedule_interval="@daily",
)

no_op_task = PythonOperator(
    task_id="task",
    python_callable=do_nothing,
    dag=my_dag,
)
