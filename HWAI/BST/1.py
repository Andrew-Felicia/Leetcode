import sys

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

#insert value into tree, return the root of the tree
def insertToBST(tree, val):
    if tree == None:
        return TreeNode(val)
    if val == '#':
        return tree
    if val <= tree.val:
        tree.left = insertToBST(tree.left, val)
    else:
        tree.right = insertToBST(tree.right, val)
    return tree

#return a list of inorder traversal of the tree
def inorder(tree):
    if tree == None:
        return []
    result = []
    result.extend(inorder(tree.left))
    result.append(tree.val)
    result.extend(inorder(tree.right))
    return result

#helper method of findAncestor, return a list of the path from root to val, but not include val.
def findAncestorRec(tree, val, path):
    if tree.val == val:
        return path
    elif tree.val < val:
        return findAncestorRec(tree.right, val, path + [tree.val])
    else:
        return findAncestorRec(tree.left, val, path + [tree.val])

#return a list of the ancestor of val, which is the path.
def findAncestor(tree, val):
    if tree == None:
        return []
    return findAncestorRec(tree, val, [])
    



def main():
    data = sys.stdin.readline
    tree_list = []
    for i in data().split():
        if i != '#':
            tree_list.append(int(i))
        else:
            tree_list.append(i)

    u, k = map(int, data().split())

    #print(tree_list)
    root = None
    for i in tree_list:
        root = insertToBST(root, i)

    inorder_list = inorder(root)

    #print(inorder_list)
    before_u = []
    for i in inorder_list:
        if i != u:
            before_u.append(i)
        else:
            break
    #print(before_u)

    ancestor = findAncestor(root, u)

    #print(ancestor)

    s = []
    for i in range(len(before_u) - 1, -1, -1):
        if before_u[i] in ancestor:
            s.append(before_u[i])
    s.reverse()
    if k > len(s):
        print(-1)
    else:
        print(s[k - 1])




    
    
    

   

if __name__ == "__main__":
    main()