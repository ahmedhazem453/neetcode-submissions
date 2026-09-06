class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dct = {}
        ans = nums[0]
        for i in nums:
            dct[i] = 1 + dct.get( i , 0)
            if dct[i] >= dct[ans] and dct[i] >=  len(nums) // 2:
                ans = i
        return ans          