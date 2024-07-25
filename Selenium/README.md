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





