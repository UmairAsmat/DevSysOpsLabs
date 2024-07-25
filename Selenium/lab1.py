from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://aws.amazon.com/")
driver.save_screenshot("aws_website.png")

time.sleep(10)
driver.quit()
