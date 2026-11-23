class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = {}
        for x in nums:
            y = seen.get(x, 0)
            if(y != 0):
                return True
            seen[x] = 1
        return False
