import json

from airflow import DAG
from airflow.models import Variable
from airflow.operators.bash import BashOperator

from processing import get_default_args

MAIN_PATH = f'/srv/git/expert-advisor/ea'
JSON_CONFIG_PATH = f'{MAIN_PATH}/configs/strategies_configs.json'


def create_dag(config: dict):
    with DAG(dag_id=config['dag_id'],
             default_args=get_default_args(),
             schedule_interval=config['schedule_interval'],
             concurrency=1,
             max_active_runs=1,
             catchup=False) as dag:
        script_name = config['script_name']
        args = f'{Variable.get(config["admin_variable_name"])}'
        command = f'cd {MAIN_PATH} && python {script_name} ' + args
        BashOperator(
            task_id='ea',
            bash_command=command,
            dag=dag
        )

    return dag


with open(JSON_CONFIG_PATH, 'r') as reader:
    json_config = reader.read()

ea_configs = json.loads(json_config)

for ea_config in ea_configs:
    dag = create_dag(ea_config)
    globals()[ea_config['dag_id']] = dag
