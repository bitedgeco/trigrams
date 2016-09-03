# _*_ coding: utf-8 _*_


SHERLOCK_SMALL_LIST = [u"One", u"night--it", u"was", u"on", u"the",
                       u"twentieth", u"of", u"March,", u"1888--I"]


DICT_OUT = {u"test word": [u"piece", u"hat"],
            u"word piece": [u"test"],
            u"piece test": [u"word"]}


DICT_IN = {u"test word": [u"piece"],
           u"word piece": [u"test"],
           u"piece test": [u"word"]}


LIST_IN = [u'test', u'word', u'piece', u'test', u'word', u'hat']


TEXT_OUT = u"test word piece test word piece test word piece test"


def test_get_text_data():
    from trigrams import get_text_data
    assert get_text_data(u'../sherlock_small.txt')[:9] == SHERLOCK_SMALL_LIST


def test_make_dict_from_list():
    """Tests make_dict_from_list returns the expected value."""
    from trigrams import make_dict_from_list
    assert make_dict_from_list(LIST_IN) == DICT_OUT


def test_make_text_from_dict():
    """Tests make_text_from_dict returns the expected value."""
    from trigrams import make_text_from_dict
    assert make_text_from_dict(u'test word', DICT_IN, 10) == TEXT_OUT


def test_main_function():
    """Tests main function gives expected output."""
    from trigrams import main_function
    assert main_function(u'../sherlock_small.txt', 5)\
        == u'One night--it was on the'
