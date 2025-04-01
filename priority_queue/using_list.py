
class PriorityQueue:
    def __init__(self):
        self.items=[]
        
    def is_empty(self):
        return len(self.items)==0
    
    def push(self,priority,data):
        self.items.append((priority,data))
        self.items.sort()
    
    def pop(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        else:
            return self.items.pop(0)[1]
    
    def size(self):
        return len(self.items)
    
p1=PriorityQueue()
print("Size: ",p1.size())
p1.push(1,10)
p1.push(3,12)
p1.push(5,27)
p1.push(4,40)
print("Size: ",p1.size())
while not p1.is_empty():
    print("Popped: ",p1.pop())
print("Size: ",p1.size())