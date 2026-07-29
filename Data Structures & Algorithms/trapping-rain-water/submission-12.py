class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        maxl = maxr = water = 0
        
        while l < r:
            if height[l] <= height[r]:
                water += max(0, maxl - height[l])
                l += 1
                maxl = max(height[0:l])
            else:
                water += max(0, maxr - height[r])
                r -= 1
                maxr = max(height[r+1:])

        return water
            

