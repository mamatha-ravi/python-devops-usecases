
# Python DevOps Use Cases
 
Python scripts for DevOps automation tasks — GitHub API integration,
SSH automation, and EC2 infrastructure provisioning with Terraform and Python.
 
---
 
## Contents
 
| Folder | Description | Tech |
|--------|-------------|------|
| `github-api/` | Python scripts to interact with GitHub API — list repos, manage issues | Python · GitHub API |
| `paramiko_example/` | SSH automation using Paramiko — connect to EC2, run remote commands | Python · Paramiko · SSH |
| `terraform-python-ec2/` | Provision AWS EC2 instances using Python + Terraform | Python · Terraform · AWS |
 
---
 
## Use Cases
 
### 1. GitHub API Automation
```python
# List all repos, create issues, manage PRs
# using PyGitHub library
import github
g = github.Github("token")
repo = g.get_repo("mamatha-ravi/roboshop-infra-dev")
```
 
### 2. SSH Automation with Paramiko
```python
# Connect to EC2 and run commands remotely
import paramiko
ssh = paramiko.SSHClient()
ssh.connect(hostname, username='ec2-user', key_filename='key.pem')
stdin, stdout, stderr = ssh.exec_command('kubectl get pods')
```
 
### 3. Terraform + Python EC2
```python
# Provision EC2 using Terraform called from Python
import subprocess
subprocess.run(['terraform', 'init'])
subprocess.run(['terraform', 'apply', '-auto-approve'])
```
 
---
 
## How to Run
 
```bash
# Clone the repo
git clone https://github.com/mamatha-ravi/python-devops-usecases
 
# Install dependencies
pip install -r requirements.txt
 
# GitHub API example
cd github-api
python github_api.py
 
# Paramiko SSH example
cd paramiko_example
python ssh_example.py
 
# Terraform Python EC2
cd terraform-python-ec2
python ec2_provision.py
```
 
---
 
## Prerequisites
 
- Python 3.8+
- AWS credentials configured (`aws configure`)
- Terraform installed
- SSH key pair for EC2 access
 
---
 
## Tech Stack
 
Python · Boto3 · Paramiko · PyGitHub · Terraform · AWS EC2
 
---
 

## Author
 
Mamatha Ravipati
📍 Hyderabad, India
📧 mamata.r@gmail.com
🔗 [github.com/mamatha-ravi](https://github.com/mamatha-ravi)
