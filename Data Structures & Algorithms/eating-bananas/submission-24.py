from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        k2 = 1
        k1 = max(piles)            

        while k2 <= k1:
            s = 0 

            m = (k1 - k2) // 2 + k2

            for i in piles:                                  
                s += ceil(i / m)  
             

            if s > h:
                k2 = m + 1
                               
            else:
                k1 = m - 1
                  

        return k2


        

      



        
