# _*_ coding: utf-8 _*_
import pytest

SHERLOCK_SMALL = "One night--it was on the twentieth of March, 1888--I was returning from a journey to a patient (for I had now returned to civil practice), when my way led me through Baker Street. As I passed the well-remembered door, which must always be associated"

def test_get_text_data():
    from trigrams import get_text_data
    assert get_text_data(sherlock_small.txt) == SHERLOCK_SMALL
 


