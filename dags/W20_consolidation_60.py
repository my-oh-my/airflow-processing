from airflow import DAG
from airflow.models import Variable
from airflow.operators.bash import BashOperator

from processing import get_default_args

with DAG('consolidation-W20-60',
         default_args=get_default_args(),
         schedule_interval='0 8-17 * * 1-5',
         concurrency=1,
         max_active_runs=1,
         catchup=False) as dag:
    args = f'{Variable.get("W20_CONSOLIDATION_60_ARGS")}'
    command = f'cd /srv/git/expert-advisor/ea && python consolidation_runner.py ' + args
    BashOperator(
        task_id='ea',
        bash_command=command
    )
