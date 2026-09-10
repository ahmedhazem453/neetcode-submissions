class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [[0, 0]]
        ans = 0

        for h in heights:
            if stack[-1][0] <= h:
                if stack[-1][0] < h:
                    stack.append([h, 1])
                else:
                    stack[-1][1] += 1
            else:
                count = 0

                while stack[-1][0] > h:
                    height, width = stack.pop()
                    count += width
                    ans = max(ans, height * count)

                count += 1

                if stack[-1][0] == h:
                    stack[-1][1] += count
                else:
                    stack.append([h, count])

        count = 0

        while stack:
            height, width = stack.pop()
            count += width
            ans = max(ans, height * count)

        return ans