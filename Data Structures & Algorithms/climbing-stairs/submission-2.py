import math
class Solution:
    
    def climbStairs(self, n: int) -> int:
        1+1+1
        twos = 1
        ways = 1

        while (2*twos) <= n:

            ways += int((math.factorial(n-twos))/(math.factorial(n-(2*twos))*math.factorial(twos)))
            twos += 1            
            
        return ways

        


        
            