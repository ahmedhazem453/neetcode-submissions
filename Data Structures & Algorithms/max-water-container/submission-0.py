class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l , r = 0 , len(heights) - 1
        ans = 0
        while l <= r :
            ans = max(ans ,  min(heights[r]  , heights[l]) * (r - l))
            if heights[r] <= heights[l]:
                r -= 1
            else :
                l += 1
        return ans 
