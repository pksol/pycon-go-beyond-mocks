import boto3
import pytest
import moto
from botocore.exceptions import ClientError

import s3_example


@pytest.fixture
def empty_bucket():
    moto_fake = moto.mock_s3()
    try:
        moto_fake.start()
        conn = boto3.resource('s3')
        conn.create_bucket(Bucket=s3_example.BUCKET)
        yield conn
    finally:
        moto_fake.stop()


def test_move_to_unique_location_no_source_object(empty_bucket):
    with pytest.raises(ClientError) as e:
        s3_example.move_to_unique_location("something")
    assert "Not Found" in str(e)


def test_move_to_unique_location_verify_read(empty_bucket):
    source_key = "something"
    content = b'some binary data'
    empty_bucket.Object(s3_example.BUCKET, source_key).put(Body=content)

    destination_key = s3_example.move_to_unique_location(source_key)

    destination_object = empty_bucket.Object(s3_example.BUCKET, destination_key).get()
    assert content == destination_object['Body'].read()
    with pytest.raises(ClientError) as e:
        empty_bucket.Object(s3_example.BUCKET, source_key).get()
    assert "The specified key does not exist" in str(e)
