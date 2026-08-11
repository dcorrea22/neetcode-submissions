# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode(0)
        tail = result   
            
        
        while list1 and list2:
            v1 = list1.val
            v2 = list2.val
            if v1 >= v2:
                n = ListNode(v2)
                tail.next = n                
                list2 = list2.next
            else:
                n = ListNode(list1.val)
                tail.next = n                
                list1 = list1.next
            tail = tail.next

        tail.next = list1 if list1 else list2        

        return result.next
    
