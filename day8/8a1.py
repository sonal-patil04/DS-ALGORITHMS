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

            # new_node.next = temp.next                  #ANOTHER METHOD
            # temp.next = new_node
            # temp.next.prev=new_node
            # new_node.prev=temp


    def delete(self,value):
        temp = self.head
        if temp.data==value:           #first node to delete
            self.head=self.head.next
            self.head.prev=None
        else:
            while (temp.data != value and temp):
                temp = temp.next
                if temp==None:
                    print("Value is not present in the list")
                    return
            temp.prev.next=temp.next
            temp.next.prev = temp.prev
            temp=None

    # WAP to print node values in reverse order




    def display(self):
        if self.head == None:
            print("List is Empty")
        else:
            temp = self.head
            while temp != None:
                print(temp.data, end=" ")
                temp = temp.next
            print()

    
    def display_rev(self):
        temp=self.head
        print("List elements in reverse order: ",end=" ")
        while temp.next:
            temp=temp.next
        while temp:
            print(temp.data, end=" ")
            temp=temp.prev

        
            print()


l1 = SLL()

l1.append(Node(10))
l1.append(Node(20))
l1.append(Node(30))
l1.append(Node(40))

print("Original Linked List:")
l1.display()
print()

print("Reversed linked list")
l1.display_rev()
print()


print("Insertion at specific position:")
l1.insert(Node(80), 7)
l1.display()
print()

print("Deletion:")
l1.delete(10)
l1.display()


