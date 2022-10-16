from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None): # this is a constructor. it will be called when someone constructs a listnode by writing 
        # Listnode(). It invookes innit function 
        self.val = val
        self.next = next

class Solution:

    # put each class in a seperate soace =, not in the middle of a function 

    # def countNodes(self, head: Optional[ListNode]):
    #     temp = head
    #     i = 0
    #     while (temp is not None):
    #         i += 1
    #         temp = temp.next
    #     return i 

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        # you don't need to define linkedlist as a class, although you could
        # class LinkedList:
        #     self.head= None 
        #main is a name for anything that is invoked from the command line
        
        head_1 = l1
        head_2 = l2
        
        
        # Input: l1 = [2,4,3], l2 = [5,6,4]
        # head_1------>(val=2)->(val=4)->(val=3)->None
        # head_2------>(val=5)->(val=6)->(val=4)->None
        # Output: [7,0,8]
        # result_head->(val=7)->(val=0)->(val=8)->None
        # 
        # Explanation: 342 + 465 = 807.
        
 
        
        results_head : Optional[ListNode] = None
        previous_node = None
        remainder = 0
        # making a fake zero object so when the lists are not the same length it doesn't stop working 
        # This will run quicker than creating a new node with 0 in for each chunk when the linked lists 
        # are not the same length 
        fake_zero_object = ListNode(val=0,next=None)

        done = False
        while not done:
            a = head_1.val
            b = head_2.val
            # print("a:{} , b:{}, remainder:{}".format(a,b,remainder))
            
            result_digit = a + b + remainder
            
            if result_digit >9:
                result_digit -= 10
                remainder = 1
                
            else:
                remainder = 0

            new_node = ListNode(val=result_digit)
            

            if results_head is None:
                # Link the new node to the head of the results list.
                results_head = new_node
            else:
                # Link the new node to the tail of the list we have so far.
                previous_node.next = new_node

            if (head_1.next is None) and (head_2.next is None) and (remainder == 0):
                done = True     
            else:

                # Advance the list pointers along each list
                if head_1.next is not None:
                    head_1 :ListNode = head_1.next
                else: 
                    head_1 : ListNode = fake_zero_object


                if head_2.next is not None: 
                    head_2 :ListNode = head_2.next
                else:
                    head_2 :ListNode = fake_zero_object
                
                previous_node = new_node

        # we should make the while loop a for loop and 
        # make it for the i times in the longest one



        
        # you only need to give the first node - the head 
        # because it is linked to the first node. 
        
    
        #a = ListNode(1)
        #b = ListNode(7)
        #c = ListNode(4)
        #a.next = b
        #b.next = c 
        #c.next = None
        




        # linked_list = LinkedList()
        # linked_list.head = Node(1)
        # second = Node(2)
        

        # first_digit = head_1.val
        # second_digit = head_1.next.val  # Link first node with second
        # second.next = third  # Link second node with the third node
  
        return results_head
            