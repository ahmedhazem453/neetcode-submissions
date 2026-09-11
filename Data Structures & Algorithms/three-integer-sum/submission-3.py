class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ret = []
        nums.sort()
        for i in range(1 , len(nums) - 1):
            l , r  = i - 1 , i + 1
            while l >= 0 and r < len(nums):
                if nums[i] + nums[l] + nums[r] == 0:
                    if not ret or [nums[l] , nums[i] , nums[r]] not in ret :
                        ret.append([nums[l] , nums[i] , nums[r]])
                    r += 1
                elif nums[i] + nums[l] + nums[r] > 0 :
                    l -= 1
                else :
                    r += 1  
        return ret
        