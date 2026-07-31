class Solution:
    def search(self, nums: List[int], target: int) -> int:
        length = len(nums)
        i = 0
        j = length - 1
        mid = length // 2

        if target not in nums:
            return -1

        while i != j:
            if nums[mid] == target: 
                print(mid)
                return mid        
            elif nums[mid] > target:
                j = mid - 1
                mid = j // 2
                print("j", j)
            elif nums[mid] < target:
                i = mid + 1
                mid = i + ((j - i) // 2)
                print("i", i)            
            
        return i
            
        
        
            

        

     