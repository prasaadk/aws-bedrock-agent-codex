variable "region" {
  description = "AWS region to deploy resources"
  type        = string
  default     = "us-east-1"
}

variable "lambda_zip_path" {
  description = "Path to the packaged Lambda zip file"
  type        = string
  default     = "../lambda/lambda.zip"
}
