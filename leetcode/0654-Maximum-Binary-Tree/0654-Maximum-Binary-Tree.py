class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        def build(l,r):
            if l>r:
                return None
            m=l
            for i in range(l,r+1):
                if nums[i]>nums[m]:
                    m=i
            root=TreeNode(nums[m])
            root.left=build(l,m-1)
            root.right=build(m+1,r)
            return root
        return build(0,len(nums)-1)