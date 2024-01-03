class TreeNode:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val


def inorder(root):
    if(root==None):
        return
    inorder(root.left)
    print(root.val)
    print(' -> ')
    inorder(root.right)


def insert(root, val):
    if(val < root.val):
        if(root.left == None):
            root.left = TreeNode(val)
        else:
            insert(root.left, val)
    else:
        if(root.right == None):
            root.right = TreeNode(val)
        else:
            insert(root.right, val)
    return

root = None
root = TreeNode(6)
insert(root, 1)
insert(root, 100)
insert(root, -1)
insert(root, -5)
insert(root, 6)
insert(root, 20)

inorder(root)
