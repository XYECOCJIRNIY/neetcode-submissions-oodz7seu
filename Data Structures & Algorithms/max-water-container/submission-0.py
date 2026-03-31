class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        Max = 0
        while l < r:
            area = min(heights[l], heights[r]) * (r - l)
            Max = max(area, Max)
            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
        return Max



        
        