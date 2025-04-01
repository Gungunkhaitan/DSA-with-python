class Node:
    def __init__(self,item=None,prev=None,next=None):
        self.item=item
        self.prev=prev
        self.next=next
class Deque:
    def __init__(self,front=None,rear=None):
        self.front=front
        self.rear=rear
        self.count=0
        
    def is_empty(self):
        return self.count==0
    
    def insert_front(self,data):
        n=Node(data)
        if self.is_empty():
            self.front=n
            self.rear=n
        else:
            n.next=self.front
            self.front=n
        self.count +=1
        
    def insert_rear(self,data):
        n=Node(data)
        if self.is_empty():
            self.front=n
            self.rear=n
        else:
            n.prev=self.rear
            self.rear=n
        self.count +=1
    
    def delete_front(self):
        if self.is_empty():
            raise IndexError("Queue is empty.")
        elif self.count==1:
            pop_val=self.front.item
            self.front=None
            self.rear=None
        else:
            pop_val=self.front.item
            self.front=self.front.next
            self.prev=None
        self.count -=1 
        return pop_val
    
    def delete_rear(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        elif self.count==1:
            pop_val=self.rear.item
            self.front=None
            self.rear=None
        else:
            pop_val=self.rear.item
            self.rear=self.rear.prev
            self.rear.next=None
        self.count -=1
        return pop_val
    
    def get_front(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        else:
            return self.front.item
        
    def get_rear(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        else:
            return self.rear.item
        
    def size(self):
        return self.count

d1=Deque()
print("Size: ",d1.size())
d1.insert_front(1)
d1.insert_front(2)
d1.insert_rear(3)
d1.insert_rear(4)
print("Front Element: ",d1.get_front())
print("Rear Element: ",d1.get_rear())
print("Size: ",d1.size())
print("Deleted Element: ",d1.delete_front())
print("Deleted Element: ",d1.delete_rear())
print("Front Element: ",d1.get_front())
print("Rear Element: ",d1.get_rear())
print("Size: ",d1.size())
        
            