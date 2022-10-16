from solution import Solution
solution = Solution()

from assertpy import assert_that

def test_that_length_is_known():
    s :str = "dog" 
    assert_that(solution.lengthOfLongestSubstring(s)).is_equal_to(3)

def test_that_it_works_with_characters():
    s: str = "dog$1"
    assert_that(solution.lengthOfLongestSubstring(s)).is_equal_to(5)

def test_that_it_works_with_spaces():
    s: str = "dog$1 cats"
    assert_that(solution.lengthOfLongestSubstring(s)).is_equal_to(10)

def test_that_it_works_with_multiple_options():
    s: str = "dogdogs"
    assert_that(solution.lengthOfLongestSubstring(s)).is_equal_to(4)

def test_case_that_failed():
    s: str = "dvdf"
    assert_that(solution.lengthOfLongestSubstring(s)).is_equal_to(3)

def test_case_with_all_same_values():
    s: str = "bbbbbb"
    assert_that(solution.lengthOfLongestSubstring(s)).is_equal_to(1)

def test_Case_with_fail():
    s = "ohvhjdml"
    assert_that(solution.lengthOfLongestSubstring(s)).is_equal_to(6)

def test_Case_failed_case():
    s = "pwwkew" 
    assert_that(solution.lengthOfLongestSubstring(s)).is_equal_to(3)