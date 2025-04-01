class Node:
    def __init__(self,item=None,next=None):
        self.item=item
        self.next=next
class CLL:
    def __init__(self,tail=None):
        self.tail=tail
    def insert_first(self,item):
        n=Node(item)
        if self.tail==None:
            n.next=n
            self.tail=n
        else:
            n.next=self.tail.next
            self.tail.next=n
    def is_empty(self):
        return self.tail==None
    def traverse(self):
        temp=self.tail.next
        while(temp != self.tail):
            print(temp.item, end=' ')
            temp=temp.next
        print(temp.item, end=' ')
        print("\n")
    def insert_last(self,item):
        n=Node(item)
        if self.is_empty():
            n.next=n
            self.tail=n
        else:
            n.next=self.tail.next
            self.tail.next=n
            self.tail=n
    def search(self,data):
        if self.is_empty():
            return None
        else:
            temp=self.tail.next
            while(temp !=self.tail):
                if(temp.item==data):
                    return temp
                else:
                    temp=temp.next
            if(temp.item==data):
                return temp
            else:
                return None
    def insert_after(self,item,temp):
        if temp is None:
            print("Cannot insert")
        else:
            n=Node(item)
            n.next=temp.next
            temp.next=n
    def delete_first(self):
        if not self.is_empty():
             self.tail.next=self.tail.next.next
        else:
            print("Nothing to delete.")
    def delete_last(self):
        if not self.is_empty():
             temp=self.tail.next
             while temp.next !=self.tail:
                 temp=temp.next
             temp.next=self.tail.next
             self.tail=temp
                
        else:
            print("Nothing to delete.")
    def delete_after(self,data):
        if self.is_empty():
            print("Nothing to delete")
        elif self.tail.next==self.tail:
            self.tail=None
        else:
            temp=self.tail.next
            flag=0
            while temp !=self.tail:
                if temp.next.item==data:
                    temp.next=temp.next.next
                    flag=1
                    break
                elif temp.item==data:
                    self.delete_first()
                    flag=1
                    break
                else:
                    temp=temp.next
            if(flag==0):
                print("Couldnt find element.")
        
c1=CLL()
c1.insert_first(4)
c1.insert_first(6)
c1.insert_first(7)
c1.insert_first(9)
print("current list:")
c1.traverse()
c1.insert_last(11)
c1.insert_last(15)
print("current list:")
c1.traverse()
print(c1.search(7))
print(c1.search(10))
c1.insert_after(22,c1.search(6))
print("current list:")
c1.traverse()
c1.delete_last()
print("current list:")
c1.traverse()
c1.delete_after(9)
print("current list:")
c1.traverse()
c1.insert_first(9)
print("current list:")
c1.traverse()
