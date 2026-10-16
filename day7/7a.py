class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class SLL:
    def __init__(self):
        self.head = None

    def append(self, new_node):
        if self.head==None:
            self.head = new_node
        else:
            temp=self.head

            while temp.next:
                temp = temp.next
            temp.next = new_node
            new_node.prev=temp

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
            self.head.prev = new_node
            self.head=new_node
        else:
            p=1

            temp = self.head
            while(p!=pos-1 and temp.next):
                temp = temp.next
                p += 1
            if temp.next:     #last position
                temp.next.prev=new_node
            new_node.prev=temp
            new_node.next = temp.next
            temp.next = new_node

            # new_node.next = temp.next
            # temp.next = new_node
            # temp.next.prev=new_node
            # new_node.prev=temp


    # def delete(self):
    #     temp = self.head
    #     while temp != None and temp.next != None:
    #         temp.next = temp.next.next
    #         temp = temp.next


l1 = SLL()

l1.append(Node(10))
l1.append(Node(20))
l1.append(Node(30))
l1.append(Node(40))

print("Original Linked List:")
l1.display()
print()

print("Insertion at specific position:")
l1.insert(Node(80), 7)
l1.display()
print()

# print("after deleting alternate nodes:")
# l1.delete()
# l1.display()
