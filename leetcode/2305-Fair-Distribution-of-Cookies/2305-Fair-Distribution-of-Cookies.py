class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        children=[0]*k
        self.ans=float('inf')  
        def dfs(i):
            if i==len(cookies):
                self.ans=min(self.ans,max(children))
                return           
            if max(children)>=self.ans:
                return 
            for j in range(k):
                children[j]+=cookies[i]
                dfs(i+1)
                children[j]-=cookies[i]
                if children[j]==0:
                    break   
        dfs(0)
        return self.ans