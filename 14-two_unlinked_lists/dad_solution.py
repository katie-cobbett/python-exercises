from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None): # this is a constructor. it will be called when someone constructs a listnode by writing 
        # Listnode(). It invookes innit function 
        self.val = val
        self.next = next

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Protect ourselves from None parameters
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        
        # We know both lists have a list node.
        
        # eg: 
        # 2-4-3
        # 2-6-4
        # should give
        # 7-0-8
        
        # But sometimes one list may be smaller than the other
        # 2-4
        # 2-6-4
        # gives
        # 4-0-5
        
        l1_head = l1
        # print(l1_head.val)
        # print(l1_head.next.val)
        # print(l1_head.next.next.val)
        
        l2_head = l2
        
        result_head = None
        result_tail = None
        
        remainder = 0
        while (l1_head is not None) or (l2_head is not None) or (remainder>0):
            subtotal = remainder
            remainder = 0
            
            if l1_head is not None:
                subtotal += l1_head.val
                l1_head = l1_head.next
            if l2_head is not None:
                subtotal += l2_head.val
                l2_head = l2_head.next
            
            if subtotal > 9:
                remainder = 1
                subtotal -= 10
                
            result_digit = ListNode(val=subtotal)
            
            if result_head is None:
                result_head = result_digit
                result_tail = result_digit
            else:
                result_tail.next = result_digit
                result_tail = result_digit
                
        return result_head