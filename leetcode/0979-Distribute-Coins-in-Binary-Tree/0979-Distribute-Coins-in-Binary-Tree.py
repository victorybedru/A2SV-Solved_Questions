class Solution:
    def distributeCoins(self, root):
        self.moves=0
        def dfs(node):
            if not node:return 0
            l=dfs(node.left)
            r=dfs(node.right)
            self.moves+=abs(l)+abs(r)
            return node.val+l+r-1
        dfs(root)
        return self.moves