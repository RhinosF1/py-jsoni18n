"""Test the languages module."""
from jsoni18n.languages import get_available_languages, get_lang_dict


def test_lanugage_dict_is_correct():
    """Check language dict includes various expected values and not incorrect ones."""
    langdict = get_lang_dict()
    assert langdict['aaa'] == 'Ghotuo'
    assert langdict['eng'] == 'English'
    assert langdict['zzj'] == 'Zuojiang Zhuang'
    assert langdict['jil'] == 'Jilim'
    assert langdict['xkx'] == 'Karore'
    assert langdict['kla'] == 'Klamath-Modoc'
    assert langdict['kao'] == 'Xaasongaxango'
    assert langdict['mky'] == 'East Makian'
    assert langdict['fra'] == 'French'
    assert 'aaj' not in langdict


def test_get_available_languages_exists():
    """Check langlist includes valid file."""
    langlist = get_available_languages('tests/data/{}')
    assert 'eng' in langlist


def test_get_available_not_on_missing():
    """Check langlist does not include missing file."""
    langlist = get_available_languages('tests/data/{}')
    assert 'aaa' not in langlist


def test_get_available_not_on_non_lang():
    """Check langlist does not include incorrect language."""
    langlist = get_available_languages('tests/data/{}')
    assert 'aaj' not in langlist
