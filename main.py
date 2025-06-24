from dotenv import load_dotenv
import os
import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError, ClientError

# load .env into os.environ
load_dotenv()

# read AWS settings
ACCESS_KEY = os.getenv("AWS_ACCESS_KEY_ID")
SECRET_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
REGION     = os.getenv("AWS_REGION")

# create S3 client
s3 = boto3.client(
    "s3",
    aws_access_key_id=ACCESS_KEY,
    aws_secret_access_key=SECRET_KEY,
    region_name=REGION
)

def test_connection():
    try:
        resp = s3.list_buckets()
        print("Connection successful. Buckets:")
        for bucket in resp.get("Buckets", []):
            print("  -", bucket["Name"])
    except (NoCredentialsError, PartialCredentialsError):
        print("Credentials not found or incomplete.")
    except ClientError as e:
        print("Client error:", e)
    except Exception as e:
        print("Unexpected error:", e)

def upload_text(bucket_name, key, text):
    try:
        s3.put_object(Bucket=bucket_name, Key=key, Body=text.encode('utf-8'))
        print(f"Uploaded to s3://{bucket_name}/{key}")
    except (NoCredentialsError, PartialCredentialsError):
        print("Credentials not found or incomplete.")
    except ClientError as e:
        print("Upload failed:", e)

if __name__ == "__main__":
    # test listing buckets
    test_connection()
    # now upload a small text file
    upload_text(
        bucket_name="e-commerce-django-static-bucket",
        key="test_upload.txt",
        text="Hello from boto3!"
    )