from assertpy import assert_that
from solution import Solution 
solution= Solution()

def test_that_anything_is_made():
    s= "cat"
    numRows = 3
    assert_that(solution.convert(s,numRows)).is_equal_to("cat")