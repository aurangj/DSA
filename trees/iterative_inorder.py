class Node:

    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data
# Insert Node
    def insert(self, data):

        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

# [10, 14, 19, 27, 31, 35, 42]
def iterative_inorder(root):
    stack = []
    stack.append(root)
    while len(stack) > 0 :
        while root.left is not None:
            stack.append(root.left)
            root = root.left
        root = stack.pop()
        print (root.data)
        if root.right is not None:
            stack.append(root.right)
            root = root.right

# [27, 14, 10, 19, 35, 31, 42]
#[27, 14, 10, 19, 35, 31, 42]
def iterative_preorder(root):
    stack = []
    stack.append(root)
    while len(stack) > 0:
        root = stack.pop()
        print(root.data)
        if root.right is not None:
            stack.append(root.right)
        if root.left is not None:
            root = root.left
            stack.append(root)

#[10, 19, 14, 31, 42, 35, 27]
# code was copied from online... as multiple attempts did not work
def iterative_postorder(root):
    stack = []
    visited = []
    stack.append(root)
    while len(stack) > 0 :
        root = stack.pop()
        visited.append(root.data)
        if root.left is not None:
            stack.append(root.left)
        if root.right is not None:
            stack.append(root.right)
    return visited[::-1]


# Preorder traversal
# Root -> Left ->Right
def PreorderTraversal( root):
    res = []
    if root:
        res.append(root.data)
        res = res + PreorderTraversal(root.left)
        res = res + PreorderTraversal(root.right)

    return res


def PostorderTraversal(root):
    res = []
    if root:
        res = PostorderTraversal(root.left)
        res = res + PostorderTraversal(root.right)
        res.append(root.data)
    return res



if __name__ == '__main__':
    root = Node(1)
    root.insert(3)
    root.insert(4)
    root.insert(6)

    print(iterative_postorder(root))
    print(PostorderTraversal(root))










