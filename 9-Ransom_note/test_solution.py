
# Assertpy is a library that allows you to import stuff, we only want assert_that 
# The assert_that allows pytesting to be done 

from assertpy import assert_that
# Gives us assert_that(x).is_equal_to(y)
from solution import Solution

solution = Solution()

def test_simplest_false_case():
    ransom_note = "a"
    magazine = "b"
    assert_that(solution.canConstruct(ransom_note,magazine)).is_false()

def test_simple_true_case():
    ransom_note = "a"
    magazine = "a"
    assert_that(solution.canConstruct(ransom_note,magazine)).is_true()

def test_simpleish_true_case():
    ransom_note = "a"
    magazine = "ba"
    assert_that(solution.canConstruct(ransom_note,magazine)).is_true()

def test_no_magazine_gives_false():
    ransom_note = "a"
    magazine = ""
    assert_that(solution.canConstruct(ransom_note,magazine)).is_false()

def test_true_case():
    ransom_note = "aaaaaaaa"
    magazine = "aaaaaaab cat dog"
    assert_that(solution.canConstruct(ransom_note,magazine)).is_true()

def test_checking_magazine_letters_only_used_once():
    ransom_note = "aa"
    magazine = "ba"
    assert_that(solution.canConstruct(ransom_note,magazine)).is_false()

