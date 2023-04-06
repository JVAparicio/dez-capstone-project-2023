from prefect import flow
from prefect_gcp import GcpCredentials
from prefect_gcp.bigquery import bigquery_query
from make_blocks import *

@flow
def populate_bq(gcp_credentials=credentials_block, bucket_name=bucket_name, 
                        bq_dataset_name=bq_dataset_name, year=2021, ncol=21):
    
    query = f'''
        CREATE OR REPLACE EXTERNAL TABLE `{bucket_name}.{bq_dataset_name}.data-{year}-{ncol}`
        OPTIONS (
        format = 'CSV',
        field_delimiter = ',',
        allow_jagged_rows = true,
        uris = ['gs://{bucket_name}/covid/{year}/{ncol}/*-{year}.csv']
        );
        '''

    result = bigquery_query(
        query, gcp_credentials, 
    )
    return result

if __name__ == "__main__":
    populate_bq(year=2021, ncol=21)
    populate_bq(year=2022, ncol=21)
    populate_bq(year=2022, ncol=18)
