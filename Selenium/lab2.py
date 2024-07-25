# Import the Selenium webdriver and time
from selenium import webdriver
Import time

# Step 2: Initialize the WebDriver (Choose your browser)
# For example, if you're using Chrome:
driver = webdriver.Chrome()

# Step 3: Perform actions on the webpage
# Example: Open the AWS website
driver.get("https://aws.amazon.com/")

# Step 4: Capture a Screenshot
# You can use the save_screenshot() method to capture a screenshot
driver.save_screenshot("aws_website.png")
time.sleep(5)

# Step 5: Close the browser
driver.quit()
