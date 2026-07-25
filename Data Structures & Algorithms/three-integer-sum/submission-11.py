class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        i = 0
        k = len(nums) - 1
        j = k - 1         
        result = []
        nums.sort()        

        while k != 2:
            summa = nums[i] + nums[j] + nums[k]
            if (summa == 0) and (i not in (k, j) and (j not in (i, k) and (k not in (i, j)))) and ([nums[i], nums[j], nums[k]] not in result):
                result.append([nums[i], nums[j], nums[k]])                
            elif (summa >= 0) and (i < j): 
                j -= 1
            elif (summa <= 0) and (i < j):
                i += 1
            else:
                k -= 1
                j = k - 1
                i = 0
        if (nums[i] + nums[j] + nums[k] == 0) and ([nums[i], nums[j], nums[k]] not in result):
            result.append([nums[i], nums[j], nums[k]])
            
        return result
                
        
            

                