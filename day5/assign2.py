
class Node :
    def __init__(self,value):
        self.data = value
        self.next = None

class SLL :
    def __init__(self):
        self.head = None
        
    def append(self,new_node): 
        if(self.head == None):
            self.head = new_node
        else:
            temp = self.head
            while(temp.next):
                temp = temp.next
            temp.next = new_node
    
    def insert(self,new_node,pos): #insert
        if pos < 1:
            print("Invalid position")
            return

        if pos == 1:
            new_node.next = self.head
            self.head = new_node
        else:
            p = 1
            temp = self.head
            while (p < pos-1 and temp):
                temp = temp.next
                p += 1

            if temp == None:
                print("Invalid position")
                return

            new_node.next = temp.next
            temp.next = new_node

    def delete(self, value):
        temp = self.head
        prev = None

        if temp == None:
            print("List is empty")
            return

        if temp.data == value:
            self.head = self.head.next
        else:
            while temp and temp.data != value:
                prev = temp
                temp = temp.next

            if temp == None:
                print("Value is not present in the list")
                return

            prev.next = temp.next
            temp = None

    def display(self):
        temp = self.head
        while(temp):
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

    # Find middle node
    def middle(self):
        slow = self.head
        fast = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        if slow:
            print("Middle node:", slow.data)
        else:
            print("List is empty")

    # Reverse linked list
    def reverse(self):
        prev = None
        temp = self.head

        while temp:
            next_node = temp.next
            temp.next = prev
            prev = temp
            temp = next_node

        self.head = prev

    # Sum of every two consecutive nodes
    def consecutive_sum(self):
        temp = self.head

        while temp and temp.next:
            total = temp.data + temp.next.data
            print(temp.data, "+", temp.next.data, "=", total)
            temp = temp.next


list1 = SLL()

n1 = Node(10)
n2 = Node(20)

list1.append(n1)
list1.append(n2)
list1.append(Node(30))
list1.append(Node(40))

print("Original Linked List:")
list1.display()

# Insert
list1.insert(Node(10), 1)
print("\nAfter insertion:")
list1.display()

# Delete
list1.delete(10)
print("\nAfter deletion:")
list1.display()

list1.delete(60)

# Middle node
print()
list1.middle()

# Consecutive sum
print("\nConsecutive sums:")
list1.consecutive_sum()

# Reverse
print("Reversed Linked List:")
list1.reverse()
list1.display()
