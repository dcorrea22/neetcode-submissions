from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        k2 = 0
        k1 = 0
        upper_bound = [0] * (len(piles))        
        max_k = max(piles)
        k1 = max_k        

        while True:
            if k1 == 0:
                break                      
            for i in range(len(piles)):                
                   
                upper_bound[i] = ceil(piles[i] / k1)
                
            s = ((sum(upper_bound)))  

            if s <= h:
                k2 = k1
                k1 = k1 // 2

            elif ceil((k1 + k2) / 2) < k2:
                k1 = ceil((k1 + k2) / 2)
                        
            else:
                break
                                 

        return k2


        

      



        
