class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n= len(nums)
        freq={}
        for num in nums:
            if num in freq:
                freq[num]+=1
            else:
                freq[num]=1
        for key in freq:
            if freq[key]> n//2:
                return key