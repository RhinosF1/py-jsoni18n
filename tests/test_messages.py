from pytest import fixture

from jsoni18n.messages import getMessages


@fixture
def get_message_location():
    return "tests/data/{}.json"


def test_base_english(get_message_location):
    messages = getMessages('eng', get_message_location)
    assert messages == {"message1": "testmessageforstart", "hello": "hello"}


def test_messages_french(get_message_location):
    messages = getMessages('fra', get_message_location)
    assert messages == {"message1": "testmessageforstart", "hello": "salut"}


def test_fails_on_non_existent(get_message_location):
    failed = False
    try:
        getMessages('aaa', get_message_location)
    except ValueError as e:
        failed = True
        assert str(e) == "Language is not available"
    assert failed


def test_fails_on_lang_invalid_but_message_exists(get_message_location):
    failed = False
    try:
        getMessages('aaj', get_message_location)
    except ValueError as e:
        failed = True
        assert str(e) == "Language is not available"
    assert failed


def test_fails_on_lang_invalid_and_no_message(get_message_location):
    failed = False
    try:
        getMessages('aam', get_message_location)
    except ValueError as e:
        failed = True
        assert str(e) == "Language is not available"
    assert failed
