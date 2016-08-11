# _*_ coding: utf-8 _*_
import pytest
import io
SHERLOCK_SMALL_LIST = ["One",  "night--it", "was", "on", "the", "twentieth", "of", "March,", "1888--I"]

def test_get_text_data():
    from trigrams import get_text_data
    assert get_text_data('src/sherlock_small.txt') == SHERLOCK_SMALL_LIST
 

def test_make_dict_from_list():
    from trigrams import make_dict_from_list
    assert make_dict_from_list(['test', 'word', 'piece', 'test', 'word', 'hat']) == {"test word": ["piece", "hat"], "word piece": ["test"], "piece test": ["word"]}


def test_make_text_from_dict():
    from trigrams import make_text_from_dict
    assert make_text_from_dict('test word', {"test word": ["piece"], "word piece": ["test"], "piece test": ["word"]}, 10) == "test word piece test word piece test word piece test"


def test_main_function():
    from trigrams import main_function
    assert main_function('src/sherlock_small.txt', 5) == 'One night--it was on the'