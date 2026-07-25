class Solution:
    def maxArea(self, heights: List[int]) -> int:
        volume = 0
        i = 0
        j = len(heights) - 1

        while i < j:
            vol = (j-i) * min(heights[i], heights[j])
            if vol > volume:
                volume = vol
            if heights[i] <= heights[j]:
                i += 1
            else:
                j -= 1

        return volume

        
        