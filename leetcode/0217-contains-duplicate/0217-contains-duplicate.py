class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        freq= {}
        for num in nums:
            if num in freq:
                return True
            freq[num]=1
        return False