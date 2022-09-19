from word_wrap_file import wrap
import pytest
from assertpy import assert_that
#columns was actually equal to the number of columns 

def test_rediculously_long_string_gets_cut_up2():
    assert_that( wrap(input="fluffycatisnice",columns=6) ).is_equal_to("fluff-\nycati-\nsnice")

