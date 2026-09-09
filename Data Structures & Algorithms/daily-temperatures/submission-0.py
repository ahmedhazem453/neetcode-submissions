class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        stack = []

        for idx in range(len(temperatures) - 1, -1, -1):
            while stack and temperatures[stack[-1]] <= temperatures[idx]:
                stack.pop()

            ans[idx] = stack[-1] - idx if stack else 0
            stack.append(idx)

        return ans