class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class SLL:
    def __init__(self):
        self.head = None
    def append(self, new_node):
        temp = self.head
        if self.head == None:
            self.head = new_node
        else:
            while temp.next != None:
                temp = temp.next
            temp.next = new_node
    def display(self):
        if self.head == None:
            print("List is Empty")
        else:
            temp = self.head
            while temp != None:
                print(temp.data, end=" ")
                temp = temp.next
            print()
    def insert(self, new_node, pos):
        if pos == 1:
            new_node.next = self.head
            self.head = new_node
        else:
            temp = self.head
            i = 1
            while i < pos - 1 and temp != None:
                temp = temp.next
                i = i + 1
            if temp == None:
                print("Invalid Position")
            else:
                new_node.next = temp.next
                temp.next = new_node
    def delete(self):
        temp = self.head
        while temp != None and temp.next != None:
            temp.next = temp.next.next
            temp = temp.next


l1 = SLL()

l1.append(Node(10))
l1.append(Node(20))
l1.append(Node(30))
l1.append(Node(40))

print("Original Linked List:")
l1.display()
print()

print("Insertion at 3rd position:")
l1.insert(Node(25), 3)
l1.display()
print()

print("after deleting alternate nodes:")
l1.delete()
l1.display()
