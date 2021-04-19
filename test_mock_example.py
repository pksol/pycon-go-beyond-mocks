from mock_example import charge_customer


def test_charge_several_items(mocker):
    mock_create = mocker.MagicMock(name='create')
    mocker.patch('mock_example.stripe.Charge.create', new=mock_create)

    charge_customer("credit_card_details", 10, 2)

    mock_create.assert_called_once_with(
        amount=20,
        currency='usd',
        source='credit_card_details')
