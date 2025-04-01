class Stack:
    def __init__(self):
        self.items=[]
    def empty(self):
        return len(self.items)==0
    def size(self):
        return len(self.items)
    def push(self,data):
        self.items.append(data)
    def pop(self):
        if not self.empty():
            print("Element removed: ",self.items[-1])
            self.items.pop()
        else:
            raise IndexError("Stack is empty")
    def peek(self):
        return self.items[-1]

s1=Stack()
print("Size: ",s1.size())
s1.push(9)
s1.push(3)
s1.push(4)
s1.push(5)
print("Top element: ",s1.peek())
print("Size: ",s1.size())
s1.pop()
print("Size: ",s1.size())
            