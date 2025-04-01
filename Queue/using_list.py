class Queue:
    def __init__(self):
        self.items=[]
    def is_empty(self):
        return len(self.items)==0
    def enqueue(self,data):
        self.items.append(data)
        print(data,"enqueued ")
    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
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

q1=Queue()
print("Size: ",q1.size())
q1.enqueue(4)
q1.enqueue(5)
q1.enqueue(6)
print("Size: ",q1.size())
print("Element Dequeued: ",q1.dequeue())
print("Front element: ",q1.get_front())
print("Rear Element: ",q1.get_rear())

