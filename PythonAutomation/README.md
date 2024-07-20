**Lab 1 - Setting up AWS EC2 for Python Development**

*Objectives:
Tasks:
1- Ec2 instance launch/configuration
2- SSH into linux
3- instal python3 and python pip and package manager

**Lab 2: Basic Python Script to Interact with AWS Services**

*Objectives: Write a Python script using Boto3 to list all your S3 buckets*

Task1: Install and configure boto3

	1.1: Install boto3
 
		Command: pip install boto3
  
             1.2: Aws Cli  Installation and Configuration
	     
		1.2.1: Aws cli installation:
  
			Command1: curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"	
   
Command2: unzip awscliv2.zip

Command3: sudo ./aws/install

1.2.2: aws configure:

	Command1: aws configure(after running this command you would be asked to input your access key and security key along with your default region
