from selenium import webdriver
import time

# Define the capabilities (browser, platform)
capabilities = {
    "browserName": "chrome",
    "platform": "LINUX"
}

options = webdriver.ChromeOptions()
options.set_capability("browserName", "chrome")
options.set_capability("platform", "LINUX")

# Start the browsers, make sure to replace your Public IPs
driver1 = webdriver.Remote(
    command_executor='http://172.31.19.249:4444/wd/hub',
    options=options
)

driver2 = webdriver.Remote(
    command_executor='http://172.31.19.249:4444/wd/hub',
    options=options
)

# Close the browsers
time.sleep(5)
driver1.quit()
driver2.quit()
