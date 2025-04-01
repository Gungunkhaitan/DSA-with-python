class Node:
    def __init__(self, item=None, left=None, right=None):
        self.left = left
        self.right = right
        self.item = item

class BinaryTree:
    def __init__(self, root=None):
        self.root = Node(root)

    def insert(self, data):
        if self.root.item:
            self._insert(data, self.root)
        else:
            self.root.item = data

    def _insert(self, data, root):
        if data < root.item:
            if root.left is None:
                root.left = Node(data)
            else:
                self._insert(data, root.left)
        elif data > root.item:
            if root.right is None:
                root.right = Node(data)
            else:
                self._insert(data, root.right)

    def inorder_traversal(self, start, traversal):
        if start:
            traversal = self.inorder_traversal(start.left, traversal)
            traversal.append(start.item)
            traversal = self.inorder_traversal(start.right, traversal)
        return traversal

    def preorder_traversal(self, start, traversal):
        if start:
            traversal.append(start.item)
            traversal = self.preorder_traversal(start.left, traversal)
            traversal = self.preorder_traversal(start.right, traversal)
        return traversal

    def postorder_traversal(self, start, traversal):
        if start:
            traversal = self.postorder_traversal(start.left, traversal)
            traversal = self.postorder_traversal(start.right, traversal)
            traversal.append(start.item)
        return traversal

bt = BinaryTree(10)
bt.insert(5)
bt.insert(15)
bt.insert(3)
bt.insert(7)
bt.insert(12)
bt.insert(18)


inorder_result = bt.inorder_traversal(bt.root, [])
print("Inorder traversal:", inorder_result)

preorder_result = bt.preorder_traversal(bt.root, [])
print("Preorder traversal:", preorder_result)

postorder_result = bt.postorder_traversal(bt.root, [])
print("Postorder traversal:", postorder_result)
