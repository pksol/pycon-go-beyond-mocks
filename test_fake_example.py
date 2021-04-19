from datetime import datetime
import pytest

from fake_example import login, create_user


@pytest.fixture
def init_users_table(mocker):
    users = {}

    def fake_add_user(username, hashed):
        users[username] = {"created_at": datetime.now(), "hashed": hashed}

    mock_add_user = mocker.MagicMock(name='add_user')
    mock_add_user.side_effect = fake_add_user
    mocker.patch('fake_example.users_table.add_user', new=mock_add_user)

    mock_get_user = mocker.MagicMock(name='get_user')
    mock_get_user.side_effect = lambda username: users.get(username, None)
    mocker.patch('fake_example.users_table.get_user', new=mock_get_user)


def test_login_non_existing_user(init_users_table):
    assert not login("made_up_user", "made_up_password")


def test_login_bad_password(init_users_table):
    create_user("made_up_user", "made_up_password")
    assert not login("made_up_user", "bad_password")


def test_login_success(init_users_table):
    create_user("made_up_user", "made_up_password")
    assert login("made_up_user", "made_up_password")








