
variable "project" {
}

variable "credentials_file" {
  # default = file(var.credentials_file)
}

variable "region" {
  default = "us-central1"
}

variable "zone" {
  default = "us-central1-c"
}

variable "bucket_name" {
}

variable "bucket_location" {
  default = "US"
}

variable "bq_dataset_name" {
}
