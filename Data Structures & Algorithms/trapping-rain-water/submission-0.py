class Solution:
    def trap(self, height: List[int]) -> int:
        l, ans = 0, 0
        n = len(height)

        while l < n and height[l] == 0:
            l += 1

        while l < n - 1:

            r = l + 1
            highest = r

            # Search for a right wall >= left wall
            while r < n and height[r] < height[l]:

                if height[r] >= height[highest]:
                    highest = r

                r += 1

            # Found a wall >= height[l]
            if r < n:
                ans += (r - l - 1) * height[l]

                for i in range(l + 1, r):
                    ans -= height[i]

                l = r

            # No wall >= height[l]
            else:
                # Use the highest wall we found
                r = highest

                for i in range(l + 1, r):
                    ans += height[r] - height[i]

                l = r

        return ans