from selenium import webdriver
import time
import boto3

# Initialize the WebDriver (e.g., Chrome)
driver = webdriver.Chrome()

# Open the webpage you want to monitor
driver.get("https://example.com")

# Measure page load time
start_time = time.time()
driver.get("https://example.com")
end_time = time.time()
load_time = end_time - start_time

# Initialize the CloudWatch client
cloudwatch = boto3.client('cloudwatch',
                         aws_access_key_id='YOUR_ACCESS_KEY_ID',
                         aws_secret_access_key='YOUR_SECRET_ACCESS_KEY',
                         region_name='YOUR_REGION')

# Push the metric to CloudWatch
cloudwatch.put_metric_data(
    Namespace='WebPerformance',
    MetricData=[
        {
            'MetricName': 'PageLoadTime',
            'Value': load_time,
            'Unit': 'Seconds',
            'Dimensions': [
                {
                    'Name': 'WebPage',
                    'Value': 'example.com'
                },
            ]
        },
    ]
)

# Close the browser
driver.quit()
