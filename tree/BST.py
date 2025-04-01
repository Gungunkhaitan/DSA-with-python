class Node:
    def __init__(self,item=None,left=None,right=None):
        self.item=item
        self.left=left
        self.right=right

class BST:
    def __init__(self,root=None):
        self.root=root
        
    def insert(self,data):
        self.root=self.rinsert(self.root,data)
    
    def rinsert(self,root,data):
        if not root:
            return Node(data)
        if data<root.item:
            root.left= self.rinsert(root.left,data)
        else:
            root.right= self.rinsert(root.right,data)
        return root
        
    def search(self,data):
        return self.rsearch(self.root,data)
    
    def rsearch(self,root,data):
        if not Node or root.item==data:
            return root
        if data<root.data:
            return self.rsearch(root.left,data)
        else:
            return self.rsearch(root.right,data)
        
    def preorder(self):
        result=[]
        self.rpreorder(self.root,result)
        return result
    
    def rpreorder(self,root,result):
        if root:
            result.append(root.item)
            self.rpreorder(root.left,result)
            self.rpreorder(root.right,result)

b=BST()
b.insert(5)
b.insert(6)
print(b.preorder())
print(b.search(5))
            
        
            