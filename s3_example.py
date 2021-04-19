import uuid

import boto3

BUCKET = "MY_BUCKET"
_s3 = boto3.client('s3')


def move_to_unique_location(source_key):
    """Moves the source key object to some fancy new destination
    in the form of 'a4a8ec45/3c6f/4a75/b7d7/112611f302'
    """
    destination_key = str(uuid.uuid4()).replace('-', '/')
    _s3.copy_object(
        CopySource=BUCKET + '/' + source_key,
        Bucket=BUCKET,
        Key=destination_key)
    _s3.delete_object(Bucket=BUCKET, Key=source_key)
    return destination_key
