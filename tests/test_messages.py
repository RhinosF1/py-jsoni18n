"""Test messages function."""
from pytest import fixture

from jsoni18n.messages import get_messages


@fixture
def get_message_location():
    """Store location of message file."""
    return "tests/data/{}.json"  # noqa: DAR101, DAR201


def test_base_english(get_message_location):
    """Test collection of english file."""  # noqa: DAR101, DAR201
    messages = get_messages('eng', get_message_location)
    assert messages == {"message1": "testmessageforstart", "hello": "hello"}


def test_messages_french(get_message_location):
    """Test collection of french override file."""   # noqa: DAR101, DAR201
    messages = get_messages('fra', get_message_location)
    assert messages == {"message1": "testmessageforstart", "hello": "salut"}


def test_fails_on_non_existent(get_message_location):
    """Test correct failure on non existent file."""   # noqa: DAR101, DAR201
    failed = False
    try:
        get_messages('aaa', get_message_location)
    except ValueError as e:
        failed = True
        assert str(e) == "Language is not available"
    assert failed


def test_fails_on_lang_invalid_but_message_exists(get_message_location):
    """Test correct failure on invalid language with messages."""  # noqa: DAR101, DAR201
    failed = False
    try:
        get_messages('aaj', get_message_location)
    except ValueError as e:
        failed = True
        assert str(e) == "Language is not available"
    assert failed


def test_fails_on_lang_invalid_and_no_message(get_message_location):
    """Test correct failure on invalid language with no messages."""  # noqa: DAR101, DAR201
    failed = False
    try:
        get_messages('aam', get_message_location)
    except ValueError as e:
        failed = True
        assert str(e) == "Language is not available"
    assert failed
