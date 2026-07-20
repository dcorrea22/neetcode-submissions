class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total = 1
        zerocount = 0

        for num in nums:
            if num != 0:
                total *= num
            else:
                zerocount += 1

        result = []
        for i in nums:
            if zerocount == 1:
                if i != 0:
                    result.append(0)
                else:
                    result.append(total)
            elif zerocount > 1:
                result.append(0)
            else:
                result.append(total // i)
        return result