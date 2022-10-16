# Assertpy is a library that allows you to import stuff, we only want assert_that 
# The assert_that allows pytesting to be done 
from assertpy import assert_that
# Gives us assert_that(x).is_equal_to(y)
from solution import Solution
solution = Solution()
#this cuts an object in memory and gives a variable called solution which points to it 

# n == colors.length == neededTime.length
# 1 <= n <= 105
# 1 <= neededTime[i] <= 104
# colors contains only lowercase English letters.

def test_dont_remove_anything_simple():
    colors= "a" 
    neededTime = [1,2]
    assert_that(solution.minCost(colors,neededTime)).is_equal_to(0)
    # you don't need to add the self when you call the minCost function here
    # you are passed the reference to the solution and its called self 
    # so it looks different depending on whether you're on the calling 
    # side or the called side. 

def test_one_to_remove_a_balloons():
    colors= "aa" 
    neededTime = [2,3]
    assert_that(solution.minCost(colors,neededTime)).is_equal_to(2)

def test_one_to_remove_a_balloons_different_costs():
    colors= "aa" 
    neededTime = [4,3]
    assert_that(solution.minCost(colors,neededTime)).is_equal_to(3)

def test_one_to_remove_b_balloons():
    colors= "abb" 
    neededTime = [2,3,1]
    assert_that(solution.minCost(colors,neededTime)).is_equal_to(1)

def test_one_to_remove_lots_of_balloons_in_pairs():
    colors= "abbccdd" 
    neededTime = [2,3,5,4,1,7,4]
    assert_that(solution.minCost(colors,neededTime)).is_equal_to(3+1+4)

def test_one_to_remove_lots_of_balloons_in_triples():
    colors= "abbbcccddd" 
    neededTime = [2, 3,5,3, 4,1,7, 4,5,6]
    assert_that(solution.minCost(colors,neededTime)).is_equal_to(3+3 + 4+1 + 4+5 )