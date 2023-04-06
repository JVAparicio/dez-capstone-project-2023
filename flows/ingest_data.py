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
def GCSUpload(day, gcs_bucket=bucket_block):

    url = f'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports_us/{day}.csv'
    http = urllib3.PoolManager(ca_certs=certifi.where())

    resp = http.request('GET', url, preload_content=False)
    csv_header = urllib3.PoolManager(ca_certs=certifi.where()).request('GET', url, preload_content=False).readline()
    ncol = csv_header.split(b'\n')[0].count(b',')+1
    year = day.split('-')[2]

    if ncol == 18:
        
        df = pd.read_csv(url)
        df['Date'] =  pd.to_datetime([day]*df.shape[0], format='%m-%d-%Y')
        filename = f"{url.split('/')[-1]}"
        bucket_path = f"covid/{year}/{ncol}/{filename}"
        bucket_block.upload_from_file_object(
            BytesIO(df.to_csv(index=False).encode('utf-8')), bucket_path
        )
    
    else:
        filename = f"{url.split('/')[-1]}"
        bucket_path = f"covid/{year}/{ncol}/{filename}"
        bucket_block.upload_from_file_object(
            resp, bucket_path
        )

    resp.release_conn()


@flow(task_runner=DaskTaskRunner(cluster_kwargs={"n_workers": 5}))
def ingest_data() -> None:
    """The main ETL function"""

    # observation_days = pd.date_range(date(2021, 1, 1), date(2023, 1, 1)-timedelta(days=1),freq='d')
    observation_days = pd.date_range(date(2022, 12, 30), date(2023, 1, 1)-timedelta(days=1),freq='d')
    list_of_observation_days = [i.strftime("%m-%d-%Y") for i in observation_days]
    for ix, day in enumerate(list_of_observation_days):
        GCSUpload.submit(day)
        if ix%10 == 0:
            time.sleep(1)
    

if __name__ == "__main__":
    ingest_data()