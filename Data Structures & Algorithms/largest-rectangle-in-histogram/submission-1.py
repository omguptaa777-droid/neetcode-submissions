class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        n = len(heights)
        for i in range(len(heights)):
            l = i
            r = i + 1
            while l >= 0 and heights[l] >= heights[i]:
                l -= 1
            while r < n and heights[r] >= heights[i]:
                r += 1
            l += 1
            r -= 1
            area = heights[i] * (r-l+1)
            maxArea = max(maxArea,area)
        return maxArea