# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        i = head
        i.previous = None
        counter = 0

        while i.next != None:       
            j = i  
            counter += 1          
            i = i.next
            i.previous = j
        counter += 1
        result = ListNode()
        result  = head

        for _ in range(counter // 2):
            j = head.next
            i.next = j            
            head.next = i            
            i = i.previous
            head = j

        head.next = None
        head = result         

        return None
        

        








        
        
            
        


        
        
        


        
        