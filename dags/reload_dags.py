import os

from airflow import DAG
from airflow.operators.bash import BashOperator

from processing import get_default_args

dag = DAG('refresh-dags',
          default_args=get_default_args(),
          schedule_interval=None)

command = f"cd {os.getenv('HOME')}/airflow-processing && git fetch --all && git reset --hard origin/master"
task = BashOperator(
    task_id='ea',
    bash_command=command,
    dag=dag
)

task
