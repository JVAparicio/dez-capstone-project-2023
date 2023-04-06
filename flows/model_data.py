from io import BytesIO
from datetime import date, timedelta
import time 
import pandas as pd
from prefect import flow, task
from prefect_gcp import GcpCredentials
from prefect_gcp.cloud_storage import GcsBucket
from prefect_dask.task_runners import DaskTaskRunner
from prefect.task_runners import ConcurrentTaskRunner

from prefect_dbt import DbtCoreOperation

# from prefect_gcp.cloud_storage import GCSUpload
import urllib3
import certifi
from make_blocks import *


@task()
def dbt() -> None:
    dbt_init = DbtCoreOperation(
    commands=["dbt debug"],
        project_dir="dbt_project",
        dbt_cli_profile=dbt_cli_profile,
        overwrite_profiles=True)

    dbt_init.run()

    dbt_init.wait_for_completion()
    # result = dbt_init.fetch_result()
    # return result

@task()
def trigger_dbt_flow():
    # dbt_cli_profile = DbtCliProfile.load("dbt-project-prefect")
    with DbtCoreOperation(
        commands=["dbt debug", "dbt docs"],
        project_dir="dbt_project",
        dbt_cli_profile=dbt_cli_profile,
        overwrite_profiles=True
    ) as dbt_operation:
        dbt_process = dbt_operation.trigger()
        # do other things before waiting for completion
        dbt_process.wait_for_completion()
        result = dbt_process.fetch_result()
    return result


@flow()
def model_data():
    # dbt()
    trigger_dbt_flow()
    # res = trigger_dbt_flow()
    # print("RESULT: ", res)


if __name__ == "__main__":
    model_data()
