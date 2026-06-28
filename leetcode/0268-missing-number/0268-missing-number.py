class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sz= len(nums)
        for i in range(sz+1):
            if i not in nums:
                return i