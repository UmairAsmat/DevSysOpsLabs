**Lab 1: Overview of EC2**

*Objective*:
Amazon Elastic Compute Cloud (Amazon EC2) is a web service provided by Amazon Web Services (AWS) that allows you to rent virtual servers, known as "instances," in the cloud. EC2 provides scalable computing resources that can be easily configured and managed, offering a wide range of options for different computing needs. Here's an overview of EC2

**Lab 2: Basic Bash Script with Docker**

*Objective:*
Grasp fundamental interactions between Bash and Docker
1. Write a Bash script to pull an Nginx Docker image.
2. Run the Docker container via the script


**Lab 3: Conditional Bash Scripts with Docker**

*Objective:*
Certainly, here's a Bash script that checks if a Docker container is running and starts it if it's not
1. Write a script that checks if a Docker container is running.
2. If not running, the script should start it

**Lab 4: Bash Loops with Docker Image Management**

*Objective:* 
Implement loop constructs in Bash for Docker image management
Tasks:
1. Write a script that lists all Docker images.
2. Use a loop to remove each image interactively.
*Instructions:*
Make sure to save this script in a .sh file (e.g., docker_image_management.sh), grant it execute permissions (chmod +x docker_image_management.sh), and then run it using ./docker_image_management.sh in a terminal.

**Lab 5: Accepting User Inputs for Docker Operations**

*Objective: Enhance user input handling in Bash for Docker-related tasks.*

Tasks:
1. Write a script that accepts an image name as input.
2. The script then pulls and runs the Docker image.
3. The script then enter you in interactive mode.
4. The script then removes the image if you exit.

**Lab 6: Functions in Bash for Modular Docker Scripts**

*Objective: Use functions in Bash to modularize Docker operations.*

Tasks:
1. Create separate functions for Docker pull, run, and stop operations.
2. Use the functions in a main Bash script workflow.
3. The script then pulls and runs the Docker image.
4. The script then enter you in interactive mode.
5. if you type Ctrl p+q it will remove the image.

**Lab 7: Scheduling Docker Workloads with Bash and Cron**

*Objective: Use Bash and Cron to automate Docker workloads.*

Tasks:
1. Write a script to run periodic backups using a Dockerized backup tool.
2. Schedule the script using Cron.
Step 1: Create Dockerfile
Step 2: Build the Docker Image
Step 3: Script Implementation
Step 4: Scheduling with Cron


**Lab 8: Bash Scripting with AWS CLI and Docker**

*Objective: Integrate AWS CLI operations with Docker in a Bash script.*

Tasks:
1. Write a Bash script to launch an EC2 instance.
2. Once launched, SSH into the instance and run a Docker container.

Documentation:
- AWS CLI basics.
- Combining AWS operations with Docker using Bash.






