from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        k2 = 0
        k1 = 0
        s = 0        
        max_k = max(piles)
        k1 = max_k        

        while k1 > 0:                                 
            for i in range(len(piles)):                                  
                s += ceil(piles[i] / (k1))          
                
             

            if s <= h:
                k2 = k1
                k1 = k1 // 2
                s = 0                
            
            elif ceil((k1 + k2) / 2) < k2:
                k1 = ceil((k1 + k2) / 2) 
                s = 0 
            
            else:
                break        

        return k2


        

      



        
