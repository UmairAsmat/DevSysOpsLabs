from selenium import webdriver

# Configure Chrome options for headless mode
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--no-sandbox')

# Initialize the WebDriver with Chrome options
driver = webdriver.Chrome()

# Open a webpage and perform actions (e.g., capturing screenshots)
driver.get("https://alnafi.com")
driver.save_screenshot("headless_screenshot.png")

# Close the browser
driver.quit()
