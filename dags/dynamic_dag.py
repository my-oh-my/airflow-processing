import json

from airflow import DAG
from airflow.models import Variable
from airflow.operators.bash import BashOperator

from processing import get_default_args

EA_PATH = f'/srv/git/expert-advisor/ea'


def create_dag(config: dict):
    with DAG(dag_id=config['dag_id'],
             default_args=get_default_args(),
             schedule_interval=config['schedule_interval'],
             concurrency=1,
             max_active_runs=1,
             catchup=False) as dag:
        script_name = config['script_name']
        args = f'{Variable.get(config["admin_variable_name"])}'
        command = f'cd {EA_PATH} && python {script_name} ' + args
        BashOperator(
            task_id='ea',
            bash_command=command,
            dag=dag
        )

    return dag


json_config = Variable.get('DAG_DEFINITIONS')
ea_configs = json.loads(json_config)

for ea_config in ea_configs:
    dag = create_dag(ea_config)
    globals()[ea_config['dag_id']] = dag
