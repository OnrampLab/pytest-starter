import argparse
import base64
import configparser
import os

import boto3

config = configparser.ConfigParser()
config.read("pytest.ini")

aws_config = config["aws"]

aws_profile = aws_config["aws_profile"]
aws_region = aws_config["aws_region"]
production_s3_bucket_name = aws_config["production_s3_bucket_name"]
staging_s3_bucket_name = aws_config["staging_s3_bucket_name"]
dev_s3_bucket_name = aws_config["dev_s3_bucket_name"]
kms_key_id = os.getenv("KMS_KEY_ID")

session = boto3.Session(profile_name=aws_profile, region_name=aws_region)


def encrypt_data(data, target_kms_key_id):
    kms_client = session.client("kms")

    response = kms_client.encrypt(KeyId=target_kms_key_id, Plaintext=data)

    return base64.encodebytes(response["CiphertextBlob"])


def upload_to_s3(bucket_name, object_key, encrypted_data):
    s3_client = session.client("s3")

    s3_client.put_object(Bucket=bucket_name, Key=object_key, Body=encrypted_data)

    print(f"Encrypted data uploaded to S3. Bucket: {bucket_name}, Key: {object_key}")


def main():
    parser = argparse.ArgumentParser(description="Encrypt data using AWS KMS")
    parser.add_argument(
        "environment",
        type=str,
        help="Environment to save object to different S3 bucket",
    )

    args = parser.parse_args()
    environment = args.environment

    if environment == "production":
        bucket_name = production_s3_bucket_name
    elif environment == "staging":
        bucket_name = staging_s3_bucket_name
    elif environment == "dev":
        bucket_name = dev_s3_bucket_name
    else:
        raise AttributeError(f"Environment {environment} is not supported")

    file_path = f"config.yml.{environment}"

    object_key = "pytest/encrypted_config.yml"

    with open(file_path, "rb") as f:
        data = f.read()

    encrypted_data = encrypt_data(data, kms_key_id)

    upload_to_s3(bucket_name, object_key, encrypted_data)


if __name__ == "__main__":
    main()
