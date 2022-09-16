import os

from airflow import DAG
from airflow.operators.bash import BashOperator

from processing import get_default_args

dag = DAG('consolidation-ETHEREUM_5',
          default_args=get_default_args(),
          schedule_interval='*/5 * * * *',
          concurrency=1,
          max_active_runs=1,
          catchup=False)

args = f'{os.getenv("ETHEREUM_5_ARGS")}'
command = f'cd /srv/git/expert-advisor/ea && python main.py ' + args
task = BashOperator(
    task_id='ea',
    bash_command=command,
    dag=dag
)

task
