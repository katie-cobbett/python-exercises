from solution import Solution 
solution = Solution()

from assertpy import assert_that

def test_very_simple():
    nums = [1,1]
    target= 2
    assert_that(solution.twoSum(nums,target)).is_equal_to([0,1])

def test_three_inputs():
    nums = [1,1,3]
    target= 4
    assert_that(solution.twoSum(nums,target)).is_equal_to([0,2])

# need to make a test for if there is just the number we are looking for in the list 

def test_3_2_4():
    nums = [3,2,4]
    target= 6
    assert_that(solution.twoSum(nums,target)).is_equal_to([1,2])

def test_with_larger_number():
    nums = [1,7,5,2]
    target= 6
    assert_that(solution.twoSum(nums,target)).is_equal_to([0,2])

def test_with_minus_numbers():
    nums = [-3,1,3,2]
    target= 0
    assert_that(solution.twoSum(nums,target)).is_equal_to([0,2])

def test_more_complex():
    nums = [-3,1,7,-2,5,3,2]
    target= -1
    assert_that(solution.twoSum(nums,target)).is_equal_to([0,6])

def test_target_is_made_from_2_neg():
    nums = [-1,-3,-5,6]
    target = [-4]
    assert_that(solution.twoSum(nums,target)).is_equal_to([0,1])

