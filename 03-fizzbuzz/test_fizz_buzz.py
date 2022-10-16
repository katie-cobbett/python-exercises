import pytest
import types
from assertpy import assert_that
import fizz_buzz_boing 

def test_fizz_buzz_3():
    assert_that( fizz_buzz_boing.fizz_buzz_boing(1,4)).is_equal_to(["1", "2", "Fizz", "4"])

def test_fizz_buzz_5():
    assert_that( fizz_buzz_boing.fizz_buzz_boing(1,6)).is_equal_to(["1", "2", "Fizz", "4", "Buzz", "Fizz"])

def test_fizz_buzz_15():
    assert_that( fizz_buzz_boing.fizz_buzz_boing(15,15)).is_equal_to(["Fizz buzz"])
