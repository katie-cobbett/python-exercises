from assertpy import assert_that
from solution import Solution
solution = Solution()

from solution import ListNode


#Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.


# Input: 
# l1=(1)->None
# l2=(2)->None
# Output:
# result=(3)->None
def test_add_two_digits():
    l1= ListNode(1)
    l2= ListNode(2)

    node = solution.addTwoNumbers(l1,l2)

    assert_that(node.val).is_equal_to(3)
    assert_that(node.next).is_none()


# Input: 
# l1=(1)->(2)->None
# l2=(2)->(4)->None
# Output:
# result=(3)->(6)->None
def test_add_4_digits():
    l1 = ListNode(1,next=ListNode(2,None))
    l2 = ListNode(2,next=ListNode(4,None))

    first_node = solution.addTwoNumbers(l1,l2)
    second_node : ListNode = first_node.next

    assert_that(first_node.val).is_equal_to(3)
    assert_that(second_node.val).is_equal_to(6)
    assert_that(second_node.next).is_none()

def test_add_6_digits():
    l1 = ListNode(1,next=ListNode(2,next=ListNode(val=4,next=None)))
    l2 = ListNode(2,next=ListNode(4,next=ListNode(val=3,next=None)))

    first_node = solution.addTwoNumbers(l1,l2)
    second_node : ListNode = first_node.next
    third_node : ListNode = second_node.next

    assert_that(first_node.val).is_equal_to(3)
    assert_that(second_node.val).is_equal_to(6)
    assert_that(third_node.val).is_equal_to(7)
    assert_that(third_node.next).is_none()


# Input: 
# l1=(1)->(2)->(3)->None
# l2=(2)->(4)->None
# Output:
# result=(3)->(6)->(3)->None
def test_add_5_digits():
    l1 = ListNode(1,next=ListNode(2,next=ListNode(val=3,next=None)))
    l2 = ListNode(2,next=ListNode(4,None))

    first_node = solution.addTwoNumbers(l1,l2)
    second_node : ListNode = first_node.next
    third_node : ListNode = second_node.next

    assert_that(first_node.val).is_equal_to(3)
    assert_that(second_node.val).is_equal_to(6)
    assert_that(third_node.val).is_equal_to(3)
    assert_that(third_node.next).is_none()

# Input: 
# l1=(1)->(2)->None
# l2=(2)->(4)->(3)->None
# Output:
# result=(3)->(6)->(3)->None
def test_add_5_digits_long_list_2():
    l1 = ListNode(1,next=ListNode(2,None))
    l2 = ListNode(2,next=ListNode(4,next=ListNode(val=3,next=None)))

    first_node = solution.addTwoNumbers(l1,l2)
    second_node : ListNode = first_node.next
    third_node : ListNode = second_node.next

    assert_that(first_node.val).is_equal_to(3)
    assert_that(second_node.val).is_equal_to(6)
    assert_that(third_node.val).is_equal_to(3)
    assert_that(third_node.next).is_none()


# Input: 
# l1=(4)->None
# l2=(6)->None
# Output:
# result=(0)->(1)->None
def test_add_two_digits_with_remainder():
    l1= ListNode(4)
    l2= ListNode(6)

    first_node = solution.addTwoNumbers(l1,l2)

    assert_that(first_node.val).is_equal_to(0)
    assert_that(first_node.next).is_not_none()

    second_node = first_node.next
    assert_that(second_node.next).is_none
    assert_that(second_node.val).is_equal_to(1)

# Input: 
# l1=(4)->None
# l2=(6)->None
# Output:
# result=(0)->(1)->None
def test_add_lots_of_overflowing():
    l1= ListNode(1)
    l2= ListNode(9,next=ListNode(9,next=None))

    first_node = solution.addTwoNumbers(l1,l2)

    assert_that(first_node.val).is_equal_to(0)
    assert_that(first_node.next).is_not_none()

    second_node = first_node.next
    assert_that(second_node.next).is_not_none
    assert_that(second_node.val).is_equal_to(0)

    third_node = second_node.next
    assert_that(third_node.next).is_none
    assert_that(third_node.val).is_equal_to(1)