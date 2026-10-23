class Node:
    def __init__(self,value):
        self.data=value
        self.next=None

class Lqueue:
    def __init__(self):
        self.front=self.rear=None
    def enqueue(self,new_node):
        if self.rear:
            self.rear.next=new_node
            self.rear=new_node
        else:
            self.front=self.rear=new_node
    def dequeue(self):
        if self.front:
            temp=self.front
            self.front=self.front.next
            if self.front==None:
                self.rear=None
                print("Now queue is empty")
            temp=None
        else:
            print("Queue is empty")


    def print(self):
        temp=self.front
        while temp:
            print(temp.data,end=" ")
            temp=temp.next
        




q1=Lqueue()
q1.enqueue(Node(10))
q1.enqueue(Node(40))
q1.enqueue(Node(30))
q1.enqueue(Node(70))
q1.enqueue(Node(20))


q1.print()
print()

q1.dequeue()
q1.dequeue()
q1.dequeue()
q1.dequeue()
q1.dequeue()


q1.enqueue(Node(50))

print("Added value after empty queue")
q1.print()