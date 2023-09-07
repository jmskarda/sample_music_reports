"""
TODO:  This script has not been debugged because I currently do not have
       access to an S3 bucket.
"""


import boto3


S3_BUCKET = "<AWS S3 Bucket URL>"
OUTPUT_FILE = r"s3_objects.txt"


def _generate_aws_credentials() -> dict:
    """Generate AWS credentials based on the local AWS client configuration."""
    credentials = {}
    session = boto3.Session()
    session_credentials = session.get_credentials()
    frozen_credentials = session_credentials.get_frozen_credentials()
    credentials["aws_access_key_id"] = frozen_credentials.access_key
    credentials["aws_secret_access_key"] = frozen_credentials.secret_key
    credentials["aws_session_token"] = frozen_credentials.token


def _get_aws_session() -> boto3.session.Session.client:
    credentials = _generate_aws_credentials()
    aws_access_key_id = credentials["aws_access_key_id"]
    aws_secret_access_key = credentials["aws_secret_access_key"]
    aws_session_token = credentials["aws_session_token"]
    return boto3.client(
        "s3",
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key,
        aws_session_token=aws_session_token,
    )


if __name__ == "__main__":
    client = _get_aws_session()
    response: dict = client.list_objects(
        Bucket=S3_BUCKET,
    )
    s3_object_urls = response.keys
    with open(OUTPUT_FILE, "w") as outfile:
        outfile.write("\n".join(s3_object_urls))
