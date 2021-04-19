import s3_example


def test_move_to_unique_location_ensure_uniqueness(mocker):
    mock_s3 = mocker.MagicMock(name='s3')
    mocker.patch('s3_example._s3', new=mock_s3)

    destinations = set()
    for _ in range(1000):
        destinations.add(s3_example.move_to_unique_location("something"))

    assert 1000 == len(destinations)


def test_move_to_unique_location_destination_format(mocker):
    mock_s3 = mocker.MagicMock(name='s3')
    mocker.patch('s3_example._s3', new=mock_s3)
    mock_uuid4 = mocker.MagicMock(name='uuid4')
    mock_uuid4.return_value = 'a4a8ec45-3c6f-4a75-b7d7-112611f302'
    mocker.patch('s3_example.uuid.uuid4', new=mock_uuid4)

    destination = s3_example.move_to_unique_location("something")

    assert 'a4a8ec45/3c6f/4a75/b7d7/112611f302' == destination


def test_move_to_unique_location_verify_calls(mocker):
    mock_s3 = mocker.MagicMock(name='s3')
    mocker.patch('s3_example._s3', new=mock_s3)

    source_key = "something"
    destination = s3_example.move_to_unique_location(source_key)

    mock_s3.copy_object.assert_called_once_with(
        CopySource=s3_example.BUCKET + '/' + source_key,
        Bucket=s3_example.BUCKET,
        Key=destination)
    mock_s3.delete_object.assert_called_once_with(
        Bucket=s3_example.BUCKET, Key=source_key)
