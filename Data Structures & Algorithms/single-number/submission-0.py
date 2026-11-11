class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums_set = set(nums)
        nums_dict = dict.fromkeys(nums_set, 0)

        for _ in nums:
            nums_dict[_] +=1       

        return sorted(nums_dict.items(), key= lambda item: item[1])[0][0]
        