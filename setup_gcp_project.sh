# Create GCP account + project
# This will also set default project and region:
export CLOUDSDK_CORE_PROJECT="dez-capstone-"`date -I`
export CLOUDSDK_COMPUTE_REGION=us-central1
export GCP_AR_REPO=$CLOUDSDK_CORE_PROJECT
export GCP_SA_NAME="dez-user"
export GCP_BILLING_ACCOIUNT="" # enter you billing id 0X0X0X-0X0X0X-0X0X0X

gcloud projects create $CLOUDSDK_CORE_PROJECT
gcloud beta billing  projects link $CLOUDSDK_CORE_PROJECT --billing-account=$GCP_BILLING_ACCOIUNT

# enable required GCP services:
gcloud services enable iamcredentials.googleapis.com
gcloud services enable iam.googleapis.com

# add roles
gcloud iam service-accounts create $GCP_SA_NAME
export MEMBER=serviceAccount:"$GCP_SA_NAME"@"$CLOUDSDK_CORE_PROJECT".iam.gserviceaccount.com
gcloud projects add-iam-policy-binding $CLOUDSDK_CORE_PROJECT --member=$MEMBER --role="roles/iam.serviceAccountUser"
gcloud projects add-iam-policy-binding $CLOUDSDK_CORE_PROJECT --member=$MEMBER --role="roles/bigquery.admin"
gcloud projects add-iam-policy-binding $CLOUDSDK_CORE_PROJECT --member=$MEMBER --role="roles/storage.admin"
gcloud projects add-iam-policy-binding $CLOUDSDK_CORE_PROJECT --member=$MEMBER --role="roles/storage.objectAdmin"

# create JSON credentials file
gcloud iam service-accounts keys create dez-capstone.json --iam-account="$GCP_SA_NAME"@"$CLOUDSDK_CORE_PROJECT".iam.gserviceaccount.com