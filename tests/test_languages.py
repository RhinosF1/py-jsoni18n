from jsoni18n.languages import getAvailableLanguages, getLangDict


def test_lanugage_dict_is_correct():
    langdict = getLangDict()
    assert langdict['aaa'] == 'Ghotuo'
    assert langdict['eng'] == 'English'
    assert langdict['zzj'] == 'Zuojiang Zhuang'
    assert langdict['jil'] == 'Jilim'
    assert langdict['xkx'] == 'Karore'
    assert langdict['kla'] == 'Klamath-Modoc'
    assert langdict['kao'] == 'Xaasongaxango'
    assert langdict['mky'] == 'East Makian'
    assert langdict['fra'] == 'French'
    assert not langdict['aaj']


def test_get_available_languages_exists():
    langlist = getAvailableLanguages('tests/data/{}.json')
    assert 'eng' in langlist


def test_get_available_not_on_missing():
    langlist = getAvailableLanguages('tests/data/{}.json')
    assert 'aaa' not in langlist
