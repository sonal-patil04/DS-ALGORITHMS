class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

class SLL:
    def __init__(self):
        self.head = None

    def append(self, new_node):
        if self.head is None:
            self.head = new_node
            new_node.next = self.head  # Points to itself to maintain circular nature
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head

    def insert(self, new_node, pos):
        if pos == 1:
            if self.head is None:
                self.head = new_node
                new_node.next = self.head
            else:
                # Find the last node to update its next pointer to the new head
                temp = self.head
                while temp.next != self.head:
                    temp = temp.next
                
                new_node.next = self.head
                self.head = new_node
                temp.next = self.head  # Complete the circle
        else:
            p = 1
            temp = self.head
            # Check to avoid AttributeError if pos is out of bounds
            while p != pos - 1 and temp.next != self.head:
                temp = temp.next
                p += 1
            new_node.next = temp.next
            temp.next = new_node

    def print(self):
        if self.head is None:
            print("\nList is empty")
            return
        print()
        temp = self.head
        print("List elements:")
        while True:
            print(temp.data, end=" ")  # Fixed .dat to .data
            temp = temp.next
            if temp == self.head:
                break
        print()

    def delete(self,value):

# Execution
list1 = SLL()
n1 = Node(10)
n2 = Node(20)
list1.append(n1)
list1.append(n2)
list1.append(Node(30))
list1.append(Node(40))
list1.print()  # Output: 10 20 30 40 

list1.insert(Node(34), 1)
list1.print()  # Output: 34 10 20 30 40