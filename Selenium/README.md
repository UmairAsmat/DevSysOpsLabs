**Lab 1: Setting up AWS EC2 for Selenium Development**

*Objective: Set up an AWS EC2 instance for Python Selenium-based automation tasks.*

Tasks:
1. Launch an EC2 instance.
2. SSH into the instance.
3. Install Python, Selenium, and required web drivers.

*Step 1 : Launching an EC2 Instance*


Log in to your AWS account.

Go to the EC2 dashboard.

Click on "Launch Instance".

Choose an Amazon Machine Image (AMI) (e.g., Ubuntu).

Select an instance type based on your requirements. (t2-Medium)

Configure instance details (leave default if unsure).

Add storage (28 GB).

Add tags (optional).

Configure security groups (open necessary ports like 22 for SSH and 80 for web applications).

Review and launch the instance.

Create or select an existing key pair and download the private key file (.pem).

*Step 2 : SSH into the Instance.*

Select the EC2 instance and click connect from the top menu.
In the shell that opens, use following commands to Install GUI and Pycharm.

  sudo apt update
  
  sudo apt install ubuntu-gnome-desktop tightvncserver

  vncserver
  
  nano ~/.vnc/xstartup

#paste the below script in the xstartup file
 
    #!/bin/bash
    export XKL_XMODMAP_DISABLE=1
    export XDG_CURRENT_DESKTOP="GNOME-Flashback:Unity"
    export XDG_MENU_PREFIX="gnome-flashback-"
    unset DBUS_SESSION_BUS_ADDRESS
    xrdb "$HOME/.Xresources"
    gnome-session &


Press Ctrl +x, then press y, then press enter to save and exit out of nano editor.

  chmod +x ~/.vnc/xstartup
  
  vncserver -kill :1
  
  vncserver


Now set the password you want to use for VNCServer

sudo apt update

sudo apt install xrdp

sudo systemctl start xrdp

sudo systemctl enable xrdp

sudo apt install gnome-tweaks

echo "gnome-session" > ~/.xsession

sudo ufw allow 3389/tcp

sudo systemctl status xrdp

sudo systemctl status xrdp-sesman

sudo passwd ubuntu


Now set the password for ubuntu user which we will use fo Remote Desktop Connection.

open your security group attached with the EC2 machine and add inbound traffic rule on port 3389 to connect with your RDC.

*Step 3: Connecting the instance with Remote Desktop Connection.*


On your Windows machine, search for "Remote Desktop Connection" in the Start menu.
<PublicIP of EC2>:3389

After the connection succeeds enter your username e.g., ‘ubuntu’ and the password you set above for that user.


*Step 4: Installing PyCharm*


Now Open terminal from the GUI.

snap find pycharm
snap install pycharm-community --classic
apt install python3-pip
pip3 install selenium

===============================================================================

**Lab 2: Simple Web Automation Test and take screenshot of webpage**

*Objective: Write a basic Selenium test to open a browser and navigate to a website to take Screenshot.

Tasks:
1. Create a simple Selenium script.
2. Open a browser and navigate to AWS's official website.
3. Capture a screenshot of the webpage.

Open PyCharm from GUI.

Create a New Project and Virtual Environment.

Create a New Python File.

Make sure to install selenium either from Terminal of PyCharm or by clicking file and going to settings.

      from selenium import webdriver
      import time
      driver = webdriver.Chrome()
      driver.get("https://aws.amazon.com/")
      driver.save_screenshot("aws_website.png")
      
      time.sleep(10)
      driver.quit()


**Lab 3: Using AWS S3 to Store Selenium Screenshots.**

*Objective: Integrate AWS services with Selenium tasks.*

Tasks:
1. Create an S3 bucket.
2. Run Selenium script to upload screenshots to the AWS S3 bucket.


Lab 4: Automated Form Submissions

Objective: Automate the process of submitting web forms using Selenium.

Tasks:
1. Write a Selenium script to fill and submit a sample web form.
2. Store submission results or responses on AWS RDS.

Step 1: Setting Up an AWS RDS Instance

Log in to your AWS account.

Go to the RDS dashboard.

Click on "Create database".

Choose a database engine, configuration, and instance details.

Set up the master username and password.

Configure advanced settings (optional).

You can configure RDS like following

standard

mysql

free tier

my-test-db

admin
password

choose existing 21

my_test_db

Review and create the RDS instance.


**Lab 5: Parallel Execution of Tests using Selenium Grid on AWS.**

*Objective: Set up a Selenium Grid on AWS to run tests on different browsers in parallel.*

Tasks:

1. Set up Selenium Grid Hub on EC2.
2. 
3. Register multiple nodes with different browsers.
4. 
5. Run a test suite in parallel across nodes.

Step 1: Setting Up Selenium Grid Hub on EC2

Log in to your AWS account.

Launch a new EC2 instance (Choose an OS based on your preference ubuntu).

Install Java on the EC2 instance.

Download and start the Selenium Grid Hub:

    sudo apt update
    
    sudo apt install default-jre
    
    #download standalone selenium
    
    wget https://selenium-release.storage.googleapis.com/3.141/selenium-server-standalone-3.141.59.jar


Access the hub using http://<EC2-Public-IP>:4444/grid/console.

Setting up Hub and Nodes on EC2


# Start the Selenium Grid Hub on your EC2 instance.

java -jar selenium-server-standalone-3.141.59.jar -role hub

Step 2: Registering Nodes with Different Browsers

Launch multiple EC2 instances (nodes) with different configurations (e.g., different browsers and operating systems).

Install Java on each node.

Download and start the Selenium Standalone Server on each node as shown above

Type following command to register the nodes


    http://<Hub-IP>:4444/grid/register



Nodes will be registered with the hub.

Parallel Execution in Selenium

Step 3: Running a Test Suite in Parallel

You can use EC2 or Local Machine. It's totally up to you to run the test suite in parallel.


**Lab 6: Continuous Integration with Jenkins and Selenium on AWS.**

Objective: Set up a CI pipeline using Jenkins to automatically trigger Selenium tests.

Tasks:

1. Install Jenkins on EC2.

3. Create a Jenkins job to run Selenium tests.

5. Store and review test results.


**Lab 7: Monitoring Web Application Performance with Selenium and CloudWatch.**

*Objective: Monitor web application performance metrics using Selenium and send data to AWS CloudWatch.*

Tasks:

1. Develop Selenium scripts to measure web page load times.

3. Push these metrics to AWS CloudWatch.


**Lab 8: Error Reporting with Selenium and AWS SNS.**

*Objective: Send notifications on Selenium test failures using AWS SNS.*

Tasks:

1. Modify Selenium scripts to detect test failures.

3. Integrate AWS SNS to send notifications upon failures.


**Lab 9: Running Headless Selenium Tests on EC2.**

*Objective: Configure and run headless Selenium tests on an EC2 instance.*

Tasks:

1. Set up necessary dependencies on EC2.

3. Write and execute a headless Selenium test.


