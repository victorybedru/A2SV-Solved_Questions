class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left=max(weights)
        right=sum(weights)   
        def can(cap):
            d=1
            curr=0
            for w in weights:
                if curr+w>cap:
                    d+=1
                    curr=0
                curr+=w
            return d<=days   
        while left<=right:
            mid=(left+right)//2
            if can(mid):
                right=mid-1
            else:
                left=mid+1     
        return left