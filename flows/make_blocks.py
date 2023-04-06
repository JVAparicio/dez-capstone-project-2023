from os import environ
from prefect_gcp import GcpCredentials
from prefect_gcp.cloud_storage import GcsBucket
from prefect_dbt.cli import BigQueryTargetConfigs, DbtCliProfile

bucket_name = "dez-capstone-2023"
gcp_config_file = environ['GOOGLE_APPLICATION_CREDENTIALS']
credentials_block_name = "dez-capstone-2023-creds"
bq_dataset_name = "covid"
bq_block_name = "bq"
dbt_project_name = "dbt_project"
dbt_env = "dev"
dbt_profile_name = "dbt-project-prefect"


credentials_block = GcpCredentials(
    service_account_file=gcp_config_file
)
credentials_block.save(credentials_block_name, overwrite=True)

credentials_block.load('default')

bucket_block = GcsBucket(
    gcp_credentials=GcpCredentials.load(credentials_block_name),
    bucket=bucket_name
)
bucket_block.save(bucket_name, overwrite=True)


target_configs = BigQueryTargetConfigs(
    schema=bq_dataset_name,  # also known as dataset
    credentials=credentials_block,
)
target_configs.save(bq_block_name, overwrite=True)


dbt_cli_profile = DbtCliProfile(
    name=dbt_project_name,
    target=dbt_env,
    target_configs=target_configs,
)

dbt_cli_profile.save(dbt_profile_name, overwrite=True)
