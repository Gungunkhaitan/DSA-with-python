class Node:
    def __init__(self,item=None,next=None):
        self.item=item
        self.next=next
class SLL:
    def __init__(self,head=None):
        self.head=head
        
    def is_empty(self):
        return self.head==None
        
    def insert_at_first(self,item):
        n=Node(item)
        if self.head is not None:
            n.next=self.head
            self.head=n
        else:
            self.head=n
            
        
    def insert_at_last(self,item):
        n=Node(item)
        if self.head is not None:
            temp=self.head
            while temp.next is not None:
                temp=temp.next
            temp.next=n
        else:
            self.head=n
    
    def insert_in_between(self,item,data):
        n=Node(item)
        temp=self.head
        while temp is not None:
            if(temp.item==data):
                n.next=temp.next
                temp.next=n
                break
            else:
                temp=temp.next
    
    def search(self,data):
        temp=self.head
        while temp is not None:
            if(temp.item==data):
                return temp
            else:
                temp=temp.next
    
    def delete_first(self):
        self.head=self.head.next
    
    def delete_last(self):
        temp=self.head
        while temp.next.next is not None:
            temp=temp.next
        temp.next=None
    
    def delete_between(self,data):
        temp=self.head
        while temp.next is not None:
            if temp.next.item==data:
                temp.next=temp.next.next
            else:
                temp=temp.next
        
        
    def traverse(self):
        temp=self.head
        if self.head is None:
            print("No elements present")
        else: 
            while temp is not None:
              print(temp.item,end=' ')
              temp=temp.next
        print("\n")
    
    
            
s1=SLL()
s1.traverse()
s1.insert_at_first(2)
s1.insert_at_first(4)
s1.insert_at_first(6)
print("current linked list")
s1.traverse()
s1.insert_at_last(8)
print("current linked list")
s1.traverse()
s1.insert_in_between(5,4)
print("current linked list")
s1.traverse()
print("Element found at: ",s1.search(7))
print("Element found at: ",s1.search(6))
s1.delete_first()
print("current linked list")
s1.traverse()
s1.delete_last()
print("current linked list")
s1.traverse()
s1.delete_between(5)
print("current linked list")
s1.traverse()

        
