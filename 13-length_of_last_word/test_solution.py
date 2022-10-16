from assertpy import assert_that
from solution import Solution 
solution = Solution()

def test_will_find_last_word():
    s="I like cats"
    assert_that(solution.lengthOfLastWord(s)).is_equal_to(4)

def test_will_find_last_from_longer_phrase():
    s="I like cats that are fluffy"
    assert_that(solution.lengthOfLastWord(s)).is_equal_to(6)