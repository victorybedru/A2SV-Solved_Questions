class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        res= [0]* len(nums)
        summation=0
        for i in range(len(nums)):
            summation+= nums[i]
            res[i]= summation
        return res
