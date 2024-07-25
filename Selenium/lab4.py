# Import necessary modules
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import pymysql

# Set up Selenium WebDriver
driver = webdriver.Chrome()

# Navigate to the target website
driver.get("https://practicetestautomation.com/practice-test-login/")

# Wait for page elements to load (in this case, waiting for 5 seconds)
time.sleep(5)

# Find and input username
input_name = driver.find_element(By.ID, "username")
input_name.send_keys("student")

# Find and input password
input_password = driver.find_element(By.ID, "password")
input_password.send_keys("Password123")

# Find and click the submit button
submit_button = driver.find_element(By.ID, "submit")
submit_button.click()

# Wait for a short period (3 seconds) to allow the page to load
time.sleep(3)

# Close the browser
driver.quit()

# Set up connection to MySQL database
conn = pymysql.connect(
    host='my-test-db.c3ogfbfieeet.us-east-2.rds.amazonaws.com',
    user='admin',
    password='password',
    database='my_test_db'
)

cursor = conn.cursor()

# Create the table if it doesn't already exist
create_table_query = """
    CREATE TABLE IF NOT EXISTS form_submissions (
        id INT AUTO_INCREMENT PRIMARY KEY,
        username VARCHAR(255),
        password VARCHAR(255)
    )
"""
cursor.execute(create_table_query)

# Define SQL query for inserting data into the table
sql = "INSERT INTO form_submissions (username, password) VALUES (%s, %s)"
values = ("student", "Password123")

# Execute the SQL query with specified values
cursor.execute(sql, values)

# Commit the changes to the database
conn.commit()

# Close the database connection
conn.close()
