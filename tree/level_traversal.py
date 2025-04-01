class Node:
    def __init__(self,item=None,left=None,right=None):
        self.left=left
        self.right=right
        self.item=item

def level_order_traversal(root):
    if not root:
        return
    result=[]
    queue=[]
    queue.append(root)
    
    while queue:
        curr=queue.pop(0)
        result.append(curr.item)
        
        if curr.left:
            queue.append(curr.left)
        if curr.right:
            queue.append(curr.right)
    return result

if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    ans=level_order_traversal(root)
    print("Level Order Traversal of binary tree is -",ans)