class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key

def is_root(root,node):
    return root==node

def length(node):
    if node is None:
        return 0
    else:
        return 1 + length(node.left) + length(node.right)

def empty(node):
    return length(node)==0

def is_leaf(node):
    if node.left is None and node.right is None:
        return True
    else:
        return False
    
def num_children(node):
    if node.left and node.right:
        return 2
    elif node.left or node.right:
        return 1
    else:
        return 0

def children(node):
    children_keys = []
    if node.left:
        children_keys.append(node.left.key)
    if node.right:
        children_keys.append(node.right.key)
    return children_keys


def insert(node, key):
    if node is None:
        return Node(key)
    elif key < node.key:
        node.left = insert(node.left, key)
    else:
        node.right = insert(node.right, key)
    return node

def minValueNode(node):
    curr = node
    while curr.left is not None:
        curr = curr.left
    return curr

def maxValueNode(node):
    curr = node
    while curr.right is not None:
        curr = curr.right
    return curr

def deleteS(root, key):
    if root is None:
        return root
    if key < root.key:
        root.left = deleteS(root.left, key)
    elif key > root.key:
        root.right = deleteS(root.right, key)
    else:
        if root.left is None:
            temp = root.right
            root = None
            return temp
        elif root.right is None:
            temp = root.left
            root = None
            return temp
        temp = minValueNode(root.right)
        root.key = temp.key
        root.right = deleteS(root.right, temp.key)
    return root

def deleteP(root, key):
    if root is None:
        return root
    if key < root.key:
        root.left = deleteP(root.left, key)
    elif key > root.key:
        root.right = deleteP(root.right, key)
    else:
        if root.left is None:
            temp = root.right
            root = None
            return temp
        if root.right is None:
            temp = root.left
            root = None
            return temp
        temp = maxValueNode(root.left)
        root.key = temp.key
        root.left = deleteP(root.left, temp.key)
    return root


def inorderTraversal(root):
    if root is not None:
        inorderTraversal(root.left)
        print(root.key,end=" ")
        inorderTraversal(root.right)

def preorderTraversal(root):
    if root is not None:
        print(root.key,end=" ")
        preorderTraversal(root.left)
        preorderTraversal(root.right)

root = None
keys = [50, 30, 20, 40, 70, 60, 80]
for key in keys:
    root = insert(root, key)

print("Inorder Traversal before deleting:")
inorderTraversal(root)

deleteS(root,50)
print("\nInorder Traversal after deleting 50:")
inorderTraversal(root)
print("\nIs {} the root node?".format(root.key), is_root(root, root))
print("\nIs the Binary tree empty?", empty(root))
leaf_node = minValueNode(root)
print("\nIs {} a leaf node?".format(leaf_node.key), is_leaf(leaf_node))
print("\nChildren of {}: {}".format(root.key,children(root)))
node_with_no_children = maxValueNode(root)
print("\nNumber of children for {}:".format(node_with_no_children.key), num_children(node_with_no_children))
print("\nLength of the tree:", length(root))

print("\nPreOrder Traversal: ")
preorderTraversal(root)






