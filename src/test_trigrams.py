# _*_ coding: utf-8 _*_
import pytest

SHERLOCK_SMALL = "One night--it was on the twentieth of March, 1888--I was returning from a journey to a patient (for I had now returned to civil practice), when my way led me through Baker Street. As I passed the well-remembered door, which must always be associated\n"

def test_get_text_data():
    from trigrams import get_text_data
    assert get_text_data('src/sherlock_small.txt') == SHERLOCK_SMALL
 

def test_split_string_into_words():
    from trigrams import split_string_into_words
    assert split_string_into_words('test word piece') == ['test', 'word', 'piece']


def test_make_dict_from_list():
    from trigrams import make_dict_from_list
    assert make_dict_from_list(['key1a', 'key1b', 'value1', 'key2a', 'key2b', 'value2']) == {"key1a key1b": ["value1"], "key2a key2b": ["value2"]}