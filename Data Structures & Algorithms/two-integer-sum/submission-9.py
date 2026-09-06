class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums = [(value, i) for i, value in enumerate(nums)]
        nums.sort()

        l, r = 0, len(nums) - 1

        while l < r:
            total = nums[l][0] + nums[r][0]

            if total == target:
                return sorted([nums[l][1], nums[r][1]])
            elif total > target:
                r -= 1
            else:
                l += 1