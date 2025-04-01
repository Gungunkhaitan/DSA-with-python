class Node:
    def __init__(self,item=None,prev=None,next=None):
        self.prev=prev
        self.item=item
        self.next=next
class DLL:
    def __init__(self,head=None):
        self.head=head
    
    def is_empty(self):
        return self.head==None
    
    def insert_at_first(self,item):
        n=Node(item,None,self.head)
        if self.head is not None:
            self.head.prev=n
        self.head=n
    
    def insert_at_end(self,item):
        n=Node(item)
        temp=self.head
        while temp.next is not None:
            temp=temp.next
        n.prev=temp
        temp.next=n
        
    def insert_in_between(self,item,data):
        n=Node(item)
        temp=self.head
        while temp is not None:
            if(temp.item==data):
                n.next=temp.next
                n.prev=temp
                temp.next=n
                break
            else:
                temp=temp.next
                
    def delete_first(self):
        self.head=self.head.next
        self.head.prev=None
        
    def delete_at_end(self):
        temp=self.head
        while temp.next.next is not None:
            temp=temp.next
        temp.next=None
        
    def delete_in_between(self,data):
        temp=self.head
        while temp.next is not None:
            if(temp.next.item==data):
                temp.next=temp.next.next
                temp.next.prev=temp
            else:
                temp=temp.next
        
    def search(self,data):
        temp=self.head
        while temp is not None:
            if(temp.item==data):
                return temp
            else:
                temp=temp.next
           
    def traverse(self):
        temp=self.head
        while(temp is not None):
            print(temp.item, end=' ')
            temp=temp.next
        print("\n")
    
    
d1=DLL()
d1.insert_at_first(5)
d1.insert_at_first(8)
d1.insert_at_first(11)
d1.insert_at_first(14)
print("current list")
d1.traverse()
d1.insert_at_end(17)
print("current list")
d1.traverse()
d1.insert_in_between(18,8)
print("current list")
d1.traverse()
d1.delete_first()
print("current list")
d1.traverse()
d1.delete_at_end()
print("current list")
d1.traverse()
d1.delete_in_between(8)
print("current list")
d1.traverse()
print(d1.search(18))

        
        