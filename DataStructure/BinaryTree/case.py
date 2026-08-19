
#know what your recursive function do
#bad
def dfs(self, root):
        result = []
        if not root:
            return []
        if root.left == None and root.right == None:
            result.append(root.val)
        self.dfs(root.left)
        self.dfs(root.right)
        return result

#using global variable
def leafValues(self, root):
        res = []
        def dfs(node) -> None:
            if node is None:  # 空节点
                return
            if node.left is None and node.right is None:  # 叶子
                res.append(node.val)
                return
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return res

#or handle with recursive function
class Solution:
    def leafSimilar(self, root1, root2) -> bool:
        return self.dfs(root1) == self.dfs(root2)

    def dfs(self, root):
        result = []
        if not root:
            return []
        if root.left == None and root.right == None:
            result.append(root.val)
        result.extend(self.dfs(root.left))
        result.extend(self.dfs(root.right))
        return result

def dfs(self, root):
        if not root:
            return []
        if not root.left and not root.right:
            return [root.val]
        return self.dfs(root.left) + self.dfs(root.right)

###############################################################