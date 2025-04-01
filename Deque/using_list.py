class Deque:
    def __init__(self):
        self.items=[]
        
    def is_empty(self):
        return len(self.items)==0
    
    def insert_front(self,data):
        self.items.insert(0,data)
        
    def insert_rear(self,data):
        self.items.append(data)
        
    def delete_front(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            raise IndexError("Queue is empty")
        
    def delete_rear(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("Queue is empty") 
    
    def get_front(self):
        if not self.is_empty():
            return self.items[0]
        else:
            raise IndexError("Queue is empty")
    
    def get_rear(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("Queue is empty")
    
    def size(self):
        return len(self.items)

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




    