class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        set_transf = set(nums)
        lst = []
        ranger = len(nums)
        idx_off = 0

        for i in range(ranger):
            if i < ranger:                      
                diff = target - nums[i]

                if (nums[i] * 2) == target:
                    print("c")
                    if nums.count(nums[i]) == 2:
                        print("a")
                        lst.append(i)
                        a = nums[i]
                        nums.pop(i)
                        index = nums.index(a) + 1
                        lst.append(index)
                        return lst

                    elif nums.count(nums[i]) == 1:
                        print("b")
                        nums.pop(i)
                        ranger -= 1
                        idx_off += 1                  
                        continue

                elif diff in set_transf:
                    print("d")                
                    lst.append(i+idx_off)
                    index = nums.index(diff)
                    lst.append(index+idx_off)
                    break
        return sorted(lst)


            
            

        