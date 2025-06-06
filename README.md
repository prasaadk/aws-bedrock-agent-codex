# AWS Bedrock Agent Codex

This repository provides an example project for deploying an AWS Bedrock Agent using **Terraform** and **GitHub Actions**. It also includes a sample Python Lambda function that the agent can invoke to perform custom actions.

## Project structure

```
.
├── lambda/                # Python source code for the Lambda function
│   ├── app.py             # Lambda handler
│   └── requirements.txt   # Python dependencies
├── terraform/             # Terraform configuration to deploy the agent and Lambda
│   ├── main.tf
│   ├── outputs.tf
│   ├── provider.tf
│   └── variables.tf
└── .github/workflows/     # GitHub Actions workflows
    └── terraform.yml      # CI/CD pipeline
```

### Terraform

The Terraform configuration creates an IAM role, deploys the Lambda function and provides a placeholder for future Bedrock Agent resources. Customize `terraform/main.tf` once the Bedrock Agent Terraform resources become available.

Run the following commands locally to deploy:

```bash
terraform -chdir=terraform init
terraform -chdir=terraform plan
terraform -chdir=terraform apply
```

### GitHub Actions workflow

The workflow defined in `.github/workflows/terraform.yml` automatically packages the Lambda code, initializes Terraform and applies the configuration after a pull request is merged into the `main` branch.

### Lambda function

The sample Lambda function located in `lambda/app.py` simply logs the incoming event and returns a JSON payload. Extend this file with any custom logic needed by your Bedrock Agent.

## Getting started

1. Ensure you have [Terraform](https://www.terraform.io/downloads.html) installed.
2. Configure AWS credentials in your environment (e.g., using `aws configure`).
3. Package the Lambda function and apply the Terraform configuration.

This setup demonstrates how infrastructure as code and automation can be combined to manage Bedrock Agents on AWS.
