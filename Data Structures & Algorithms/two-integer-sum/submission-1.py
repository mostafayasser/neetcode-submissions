class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numbersMap = {}
        for i in range(len(nums)):
            numbersMap[nums[i]] = i
        for i, x in enumerate(nums):
            y = target - x
            if y in numbersMap and numbersMap[y] != i:
                return [i,numbersMap[y]]

        