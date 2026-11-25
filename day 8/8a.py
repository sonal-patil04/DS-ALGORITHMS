class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class doublyLinkedList:
    def __init__(self):
        self.head = None

    # Create linked list (append)
    def append(self, new_node):
        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
        new_node.prev = temp

    # Traverse and print the nodes
    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

    # reverse the linked list
    def printreverse(self):
        temp = self.head
        print("Reversed List:")
        if temp is None:
            print("None")
            return
        while temp.next:
            temp = temp.next
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.prev        
        print("None")

    # # Insert a node at a given position (0-based)
    # def insert(self, new_node, pos):
    #     if pos < 0:
    #         print("Invalid position")
    #         return

    #     if pos == 0:
    #         new_node.next = self.head
    #         if self.head:
    #             self.head.prev = new_node
    #         self.head = new_node
    #         return

    #     temp = self.head
    #     for _ in range(pos - 1):
    #         if temp is None:
    #             print("Invalid position")
    #             return
    #         temp = temp.next

    #     if temp is None:
    #         print("Invalid position")
    #         return

    #     new_node.next = temp.next
    #     temp.next = new_node
    #     if new_node.next:
    #         new_node.next.prev = new_node

    # Delete a node at a given position (0-based)
    def delete(self, pos):
        if self.head is None or pos < 0:
            print("Invalid position")
            return

        if pos == 0:
            self.head = self.head.next
            if self.head:
                self.head.prev = None
            return

        temp = self.head
        for _ in range(pos - 1):
            if temp.next is None:
                print("Invalid position")
                return
            temp = temp.next

        if temp.next is None:
            print("Invalid position")
            return

        temp.next = temp.next.next
        if temp.next:
            temp.next.prev = temp


# Create linked list
List = doublyLinkedList()

List.append(Node(10))
List.append(Node(20))
List.append(Node(30))
List.append(Node(40))
List.append(Node(50))
List.append(Node(60))
List.append(Node(70))

print("Elements:")
List.display()
print()

print("Reverse elements: ")
List.printreverse()

# List.insert(Node(8), 3)
# print("After Insertion:")
# List.display()

List.delete(0)
print("After Deletion:")
List.display()

List.printreverse()