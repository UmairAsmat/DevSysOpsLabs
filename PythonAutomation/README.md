**Lab 1: Setting up AWS EC2 for Python Development**

*Objectives:*

**Tasks:**

1- Ec2 instance launch/configuration

2- SSH into linux

3- instal python3 and python pip and package manager

**Lab 2: Basic Python Script to Interact with AWS Services**

*Objectives: Write a Python script using Boto3 to list all your S3 buckets*

**Task1:**
Install and configure boto3

1.1: Install boto3
 Command:
  
  	pip install boto3
   
  
1.2: Aws Cli  Installation and Configuration
	     
1.2.1: Aws cli installation:

  Command:
  
   	curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"	
    
   
 Command: 
 
 	unzip awscliv2.zip

 Command: 
 
 	sudo ./aws/install
   

1.2.2: aws configure:

Command: 

 	aws configure(after running this command you would be asked to input your access key and security key along with your default region


**Lab 3: Automating EC2 Instance Management with Python**

**Objective**:
Create Python scripts to start, stop, and monitor EC2 instances.

**Tasks**:
1. Write a script to start/stop an EC2 instance.
2. Extend the script to monitor CPU utilization.

**Lab 4: Python Automation for AWS RDS**

**Objective**:
Automate AWS RDS backups using Python.

**Tasks**:
1. Create an RDS instance.
2. Write a Python script to trigger manual backups.

**Lab 5 - Deploying Lambda Functions with Python**

**Objective**:

Step1:
Write a Simple Python Lambda Function

step 2:
Create a Deployment Package

step 3:
Create an IAM Role

step 4:
Attach Permissions to the IAM Role

step 5:
Create the Lambda Function

Step 5:
aws lambda invoke --function-name <your-function-name> output.txt


**Lab 6: Automating AWS S3 Operations with Python**

**Objective**:
Use Python to automate common AWS S3 tasks.

**Tasks**:
1. Write a script to upload/download files from S3.
2. Implement versioning in the script.




