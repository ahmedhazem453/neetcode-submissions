class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        dct = {}
        for i in range(len(numbers)):
            if target - numbers[i] in dct :
                return [dct[target - numbers[i]] + 1 , i + 1]
            dct[numbers[i]] = i 
      