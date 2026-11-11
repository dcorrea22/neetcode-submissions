import math
class Solution:
    
    def climbStairs(self, n: int) -> int:
        twos = 0
        ways = 0

        while (2*twos) <= n:

            ways += int((math.factorial(n-twos))/(math.factorial(n-(2*twos))*math.factorial(twos)))
            twos += 1            
            
        return ways

        


        
            