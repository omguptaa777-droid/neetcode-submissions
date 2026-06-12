class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        i = 0
        j = n - 1

        ans = 0

        while i < j:
            ans = max(ans,(j-i)*min(heights[i],heights[j]))
            if heights[i] < heights[j]:
                i += 1
            elif heights[i] > heights[j]:
                j -= 1
            else:
                if heights[i-1] <= heights[j-1]:
                    j -= 1
                else:
                    i += 1
        
        return ans
