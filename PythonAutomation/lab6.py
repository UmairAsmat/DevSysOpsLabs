import boto3

#s3 client
s3 = boto3.client('s3')


bucket_name = 'your_bucket_name'

# Create the S3 bucket
s3.create_bucket(Bucket=bucket_name)


# Replace with your specific local file, bucket name, and object key
local_file_path = 'local_file.txt'
bucket_name = 'your_bucket_name'
object_key = 'remote_file.txt'

# Upload the local file to the S3 bucket with the specified object key
s3.upload_file(local_file_path, bucket_name, object_key)
#downloading files
s3.download_file('your_bucket_name', 'remote_file.txt', 'local_file.txt')

#implementing versioning
s3.put_bucket_versioning(
    Bucket='your_bucket_name',
    VersioningConfiguration={
        'Status': 'Enabled'
    }
)

#list versioning
response = s3.list_object_versions(Bucket='your_bucket_name')
for version in response.get('Versions', []):
    print(f"Object Key: {version['Key']}, Version ID: {version['VersionId']}")
