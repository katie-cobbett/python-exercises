
import word_wrap
import pytest
from assertpy import assert_that
#columns was actually equal to the number of columns 

def test_small_string_returns_itself():
    assert_that( word_wrap.wrap(input="a",columns=4) ).is_equal_to("a")

def test_another_small_string_returns_itself():
    assert_that( word_wrap.wrap(input="b",columns=4) ).is_equal_to("b")

def test_longer_string_adds_new_lines():
    assert_that( word_wrap.wrap(input="I like cats",columns=4) ).is_equal_to("I\nlike\ncats")

def test_longer_string_adds_new_lines_long_columns():
    assert_that( word_wrap.wrap(input="I like cats",columns=6) ).is_equal_to("I like\ncats")

def test_longer_string_than_columns():
    assert_that( word_wrap.wrap(input="abcd",columns=3) ).is_equal_to("ab-\ncd")

def test_rediculously_long_string_gets_cut_up():
    assert_that( word_wrap.wrap(input="fluff",columns=3) ).is_equal_to("fl-\nuff")

