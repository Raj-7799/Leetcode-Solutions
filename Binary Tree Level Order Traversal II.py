class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        out = []
        
        def dfs(root,level):
            if not root:
                return 
            if level<len(out):
                out[level].append(root.val)
            else:
                out.append([root.val])
            dfs(root.left,level+1)
            dfs(root.right,level+1)
        
        dfs(root,0)
        return out[::-1]
        
