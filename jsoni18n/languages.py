"""Get information on langauges from pycountry."""
from pycountry import languages


def get_lang_dict():
    """Get a dict with code: name for each language that is in pycountry.

    Returns:
        dict: code: name for each alpha_3 code in pycountry
    """
    langdict = {}
    for lang in languages:
        langdict[lang.alpha_3] = lang.name
    return langdict


def get_available_languages(messageLocation):
    """Get a dict with code: name for each language that is in pycountry.

    Args:
        messageLocation (str): path to messages.  Example: /path/{}.json

    Returns:
        list: list of valid lanuages that have a file in messagelocation.
    """
    availableLanguages = []
    for langcode in get_lang_dict():
        try:
            open(messageLocation.format(langcode), 'r')
            availableLanguages.append(langcode)
        except (OSError, IOError):  # https://stackoverflow.com/a/15032444
            pass
    return availableLanguages
