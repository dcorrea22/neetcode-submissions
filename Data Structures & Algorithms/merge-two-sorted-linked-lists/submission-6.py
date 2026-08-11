# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode(0)
        tail = result
        
        if list1 == None and list2 != None:
            return list2  
        elif list2 == None and list1 != None:
            return list1
        elif list1 == None and list2 == None:
            return list1        
        
        while list1 != None and list2 != None:
            if list1.val >= list2.val:
                n = ListNode(list2.val)
                tail.next = n
                tail = tail.next
                list2 = list2.next
            else:
                n = ListNode(list1.val)
                tail.next = n
                tail = tail.next
                list1 = list1.next

        if list1 == None and list2 != None:
            while list2 != None:
                n = ListNode(list2.val)
                tail.next = n
                tail = tail.next
                list2 = list2.next
        elif list2 == None and list1 != None:
            while list1 != None:
                n = ListNode(list1.val)
                tail.next = n
                tail = tail.next
                list1 = list1.next

        result = result.next

        return result
    
