class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

class stack:
    def __init__(self):
        self.top=None
    def isempty(self):
        return self.top is None
    def push(self, new_node):
        new_node.next=self.top
        self.top=new_node
    def pop(self):
        if self.isempty():
            print("Stack is empty")
        else:
            temp=self.top
            print("Popped elements: ",temp.data)
            self.top=self.top.next
            temp=None
    def reverse_stack(self):
        temp = self.top
        while temp:
            s2.push(Node(temp.data))
            temp=temp.next

    def print(self):
        temp=self.top
        print("Stack elements...")
        while temp:
            print(temp.data)
            temp=temp.next


s1=stack()
s2=stack()
s1.push(Node(10))
s1.push(Node(99))
s1.push(Node(45))
s1.push(Node(67))
s1.push(Node(90))

# s1.pop()
# s1.pop()
# s1.pop()
# s1.pop()

s1.reverse_stack()
s1.print()
s2.print()