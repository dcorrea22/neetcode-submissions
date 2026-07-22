class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:        
        toset = set(sorted(nums))
        j = 0 
        k = 1
        print(sorted(toset))    

        for i in sorted(toset):
            print("i:", end = "")
            print(i)
                                 
            if (i + 1) in toset:
                k += 1

            else:
                if k >= j:
                    j = k
                    k = 1                    
                else:
                    k = 1                    
            print("j:", end = "")
            print(j)
            
        return j 
            
        
        