# GitHub Workflows for Infrastructure Deployment
  
This guide explains how to use the provided GitHub Actions workflows for deploying and destroying infrastructure using Terraform.
  
## Available Workflows
  
1. **deploy_infra_terraform.yml**: Handles infrastructure deployment
  2. **destroy_infra_terraform.yml**: Manages infrastructure destruction with safety checks
  
  ## Best Practices
  
  1. Always review Terraform plans before applying
  2. Use meaningful commit messages for infrastructure changes
  3. Document major infrastructure changes in pull requests
  4. Test changes in dev environment before production
  5. Keep secrets and sensitive variables in GitHub Secrets
  6. Regularly review and update access permissions

  ## Prerequisites
  
  1. Azure subscription and permissions
  2. GitHub repository with the infrastructure code
  3. Access to GitHub Actions settings
  
  ## Configuration Steps
  
  ### 1. Configure GitHub Secrets
  
  Add the following secrets in your GitHub repository (Settings → Secrets and variables → Actions → New repository secret):
  
  ```text
  # Azure Authentication
  AZURE_CLIENT_ID          # DevOps SPN Client ID
  AZURE_SUBSCRIPTION_ID    # Azure Subscription ID
  AZURE_TENANT_ID         # Azure Tenant ID
  ARM_SUBSCRIPTION_ID     # Azure Subscription ID
  
  # Terraform Variables
  TF_VAR_DEVOPS_SPN_OBJECT_ID           # Object ID of the DevOps Service Principal
  TF_VAR_TF_BACKEND_STORAGE_ACCOUNT_ID   # Storage Account ID for Terraform backend
  TF_VAR_USER_PASSWORD                   # Password for the Azure AD user
  
  # Email Notifications (for destroy workflow)
  SMTP_SERVER             # SMTP server address
  SMTP_PORT              # SMTP server port
  SMTP_USERNAME          # SMTP authentication username
  SMTP_PASSWORD          # SMTP authentication password
  EMAIL_NOTIFICATIONS    # Comma-separated list of email addresses
  ```
  
  ### 2. Configure Environment Variables
  
  The workflows use environment variables defined in the workflow files. Review and modify these in the workflow files as needed:
  
  ```yaml
  env:
    TF_WORKSPACE: \"dev\"
    TF_VAR_location: \"westeurope\"
    TF_VAR_resource_name_prefix: \"ezazml7\"
    # ... other variables
  ```
  
  ### 3. Configure Branch Protection (Recommended)
  
  1. Go to repository Settings → Branches
  2. Add branch protection rule for `main`
  3. Enable:
     - Require pull request reviews
     - Require status checks to pass
     - Include administrators in restrictions
  
  ## Using the Workflows
  
  ### Deployment Workflow
  
  The deployment workflow (`deploy_infra_terraform.yml`) runs automatically on:
  - Push to `main` branch (affecting `.tf` files)
  - Pull requests (affecting `.tf` files)
  - Manual trigger
  
  To manually trigger:
  1. Go to Actions → deploy_infra_terraform
  2. Click \"Run workflow\"
  3. Select branch
  4. Click \"Run workflow\"
  
  The workflow will:
  1. Initialize Terraform
  2. Check formatting
  3. Create execution plan
  4. Apply changes (only on `main` branch)
  
  ### Destruction Workflow
  
  The destruction workflow (`destroy_infra_terraform.yml`) is manual-only with safety checks.
  
  To trigger infrastructure destruction:
  1. Go to Actions → destroy_infra_terraform
  2. Click \"Run workflow\"
  3. Fill in required information:
     - Environment (dev/staging/prod)
     - Confirmation string (format: `DESTROY-INFRASTRUCTURE-[ENV]-[DATE]`)
     - Reason for destruction
     - Related ticket ID
  4. Click \"Run workflow\"
  
  The workflow will:
  1. Perform safety checks
  2. Notify stakeholders
  3. Wait 10 minutes
  4. Execute destruction
  5. Send completion notification
  
  ## Safety Features
  
  The destruction workflow includes several safety measures:
  - Required confirmation string
  - Business hours check (Mon-Fri, 9 AM - 5 PM)
  - User authorization verification
  - 10-minute waiting period
  - Email notifications
  - Audit logging
  
  ## Monitoring and Logs
  
  ### Deployment Logs
  - View in GitHub Actions tab
  - Check job outputs for each step
  - Terraform plans are available in job artifacts
  
  ### Destruction Audit Logs
  - Automatically uploaded as artifacts
  - Retained for 90 days
  - Include:
    - Pre-destruction state
    - Destruction plan
    - Post-destruction state
  
  ## Troubleshooting
  
  Common issues and solutions:
  
  1. **Workflow fails at Azure login**:
     - Verify Azure credentials in GitHub secrets
     - Check SPN permissions
  
  2. **Terraform initialization fails**:
     - Verify backend configuration
     - Check storage account access
  
  3. **Destruction confirmation fails**:
     - Ensure correct date format in confirmation string
     - Verify you're within business hours
  