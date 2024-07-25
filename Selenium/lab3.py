# Import necessary libraries
from selenium import webdriver
import boto3

# Initialize the S3 client
s3 = boto3.client('s3',
                  aws_access_key_id='YOUR_ACCESS_KEY_ID',
                  aws_secret_access_key='YOUR_SECRET_ACCESS_KEY',
                  region_name='YOUR_REGION')

# Initialize the WebDriver (e.g., Chrome)
driver = webdriver.Chrome()

# Open the AWS website
driver.get("https://aws.amazon.com/")

# Capture a screenshot
driver.save_screenshot("screenshot.png")

# Upload the screenshot to the S3 bucket
bucket_name = 'sel-test-bucket'
object_name = 'screenshot.png'
s3.upload_file('screenshot.png', bucket_name, object_name)

time.sleep(10)
driver.quit()
