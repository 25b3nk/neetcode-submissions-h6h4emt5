class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        d = {}
        for n in nums:
            if n not in d:
                d[n] = True
            else:
                return True
        return False
