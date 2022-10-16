from logging.config import valid_ident


class ListNode: 
    def __innit__(self, val = 0, next= None):
        self.val = val
        self.next = next

class Solution():
    def print_two_linked_lists(self, list1 : Optional[ListNode], list2 :Optional[ListNode]):
        head1= list1 
        head2= list2
        input list1= [2,3,4]
        input list2 = [3,4,5]
        
        print ("the first values of each list are {}
        while head1.next is not None: 
            tempval1= head1.val 
            tempval2 = head1.val
            print ("the next are", tempval1, tempval2)
            head1 = head1.next 
            
            

