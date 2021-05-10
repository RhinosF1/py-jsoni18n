"""Get information on langauges from pycountry."""
from pycountry import languages
from glob import glob


def get_lang_dict():
    """Get a dict with code: name for each language that is in pycountry.

    Returns:
        dict: code: name for each alpha_3 code in pycountry
    """
    langdict = {}
    for lang in languages:
        langdict[lang.alpha_3] = lang.name
    return langdict


def get_available_languages(message_location, fileformat='json'):
    """Get a dict with code: name for each language that is in pycountry.

    Args:
        message_location (str): path to messages.  Example: /path/{}
        fileformat (str): filetype. Default: json.

    Returns:
        list: list of valid lanuages that have a file in messagelocation.
    """
    available_languages = []
    for name in glob(f'{message_location.rstrip('/')}.{fileformat}'):
        lang = name[:-(len(fileformat))][len(message_location.rstrip('/')):]
        if lang in get_lang_dict():
            available_languages.append(lang)
    return available_languages
