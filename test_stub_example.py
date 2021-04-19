from stub_example import are_you_feeling_lucky


def test_are_you_feeling_lucky_yes(mocker):
    mock_randint = mocker.MagicMock(name='randint')
    mock_randint.return_value = 13
    mocker.patch('stub_example.randint', new=mock_randint)

    assert are_you_feeling_lucky()


def test_are_you_feeling_lucky_no(mocker):
    mock_randint = mocker.MagicMock(name='randint')
    mock_randint.return_value = 27
    mocker.patch('stub_example.randint', new=mock_randint)

    assert not are_you_feeling_lucky()
