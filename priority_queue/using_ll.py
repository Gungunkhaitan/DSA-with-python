class Node:
    def __init__(self,priority=None,item=None,next=None):
        self.priority=priority
        self.item=item
        self.next=None
class PriorityQueue:
    def __init__(self,head=None):
        self.head=head
        self.count=0
    def push(self,prior,data):
        n=Node(prior,data)
        curr=self.head
        self.count+=1
        if self.head is None or self.head.priority>prior:
            n.next=self.head
            self.head=n
            return
        while curr.next is not None and curr.next.priority<=prior:
            curr=curr.next
        n.next=curr.next
        curr.next=n
        
    def is_empty(self):
        return self.count==0
    
    def pop(self):
        if not self.is_empty():
            self.count-=1
            pop_val=self.head.item
            self.head=self.head.next
        else:
            raise IndexError("Queue is empty.")
        return pop_val
    
    def size(self):
        return self.count    
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