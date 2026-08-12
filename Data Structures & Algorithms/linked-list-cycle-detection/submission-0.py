# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        i = 0

        while head != None:
            try:
                print(head.index)
                return True
            except:
                head.index = i
                i += 1
                head = head.next 
                
        return False      