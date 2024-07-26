# Import necessary modules
from selenium import webdriver  # Import the Selenium WebDriver module
from selenium.webdriver.chrome.service import Service as ChromeService  # Import the ChromeService
from webdriver_manager.chrome import ChromeDriverManager  # Import the ChromeDriverManager
from selenium.webdriver.common.by import By  # Import the 'By' class for locating elements
import time  # Import the 'time' module for adding delays

# Modifying Selenium Scripts for Error Detection

# Initialize a Chrome WebDriver instance
driver = webdriver.Chrome()  # This will open a Chrome browser window

# Navigate to the specified URL
driver.get("https://alnafi.com/auth/sign-in")

try:
    # Try to locate an element with the name "email1"
    element = driver.find_element(By.NAME, "email1")

    # If the element is found, print a success message
    print("Element Found")

except:
    # If the element is not found, print an error message and mark the test as failed
    print("Element not found. Test Failed.")

# Close the browser window
driver.quit()



# Modifying Selenium Scripts for SNS Integration


driver = webdriver.Chrome()
driver.get("https://alnafi.com/auth/sign-in")
try:
    element = driver.find_element(By.NAME,"email1")
    print("Element Found")
except:
    print("Element not found. Test Failed.")


    # Initialize the SNS client
    sns = boto3.client('sns',
                      aws_access_key_id='YOUR_ACCESS_KEY_ID',
                      aws_secret_access_key='YOUR_SECRET_ACCESS_KEY',
                      region_name='YOUR_REGION')

    # Publish a message to the SNS topic
    sns.publish(
        TopicArn='arn:aws:sns:YOUR_REGION:YOUR_ACCOUNT_ID:YOUR_TOPIC_NAME',
        Message='Selenium test failed. Check logs for details.'
    )

# Close the browser
driver.quit()
