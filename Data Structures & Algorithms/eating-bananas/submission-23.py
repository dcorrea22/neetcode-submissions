from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        k2 = 0
        k1 = max(piles)            

        while k1 > 0:
            s = 0 

            for i in piles:                                  
                s += ceil(i / (k1))  
             

            if s <= h:
                k2 = k1
                k1 = k1 // 2
                               
            
            elif ceil((k1 + k2) / 2) < k2:
                k1 = ceil((k1 + k2) / 2) 
                
            
            else:
                break        

        return k2


        

      



        
