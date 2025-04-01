class CircularQueue:
    def __init__(self,capacity):
        self.capacity=capacity
        self.queue=[None]*capacity
        self.front=self.rear=-1
    
    def is_full(self):
        return (self.rear+1)%self.capacity==self.front
    
    def is_empty(self):
        return self.front==-1
    
    def enqueue(self,data):
        if self.is_full():
            print("Queue is full. can't enqueue")
            return 
        elif self.is_empty():
            self.front=0
            self.rear=0
        else:
            self.rear=(self.rear+1)%self.capacity
        self.queue[self.rear]=data
    
    def dequeue(self):
        if self.is_empty():
            print("Cant Dequeue. Queue is empty.")
            return
        popped=self.queue[self.front]
        if self.front==self.rear:
            self.front=self.rear=-1
        else:
            self.front=(self.front+1)%self.capacity
        return popped
    
    def peek(self):
        return self.queue[self.front]
    
    def display(self):
        if self.is_empty():
            print("Queue is empty.")
        elif self.front<=self.rear:
            for i in range(self.front,self.rear+1):
                print(self.queue[i]," ")
        else:
            for i in range(self.front,self.capacity):
                print(self.queue[i])
            for i in range(0,self.rear):
                print(self.queue[i])

queue = CircularQueue(5)

queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
queue.enqueue(5)

queue.display()

print("Popped: ",queue.dequeue())
print("Popped: ",queue.dequeue())

queue.display()

queue.enqueue(6)
queue.enqueue(7)

queue.display()
            
    
    