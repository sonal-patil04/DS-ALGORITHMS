class Node :
    def __init__(self,value):
        self.data = value
        self.next = None

class SLL :
    def __init__(self):
        self.head = None


    # inserting value
    def insert(self,new_node): #print
        if(self.head == None):
            self.head = new_node
        else:
            temp = self.head
            while(temp.next):
                temp = temp.next
            temp.next = new_node



    #adding value at specific position

    def append(self, new_node, pos):
        if pos ==1:
            new_node.next = self.head
            self.head = new_node
        else:
            p = 1
            temp = self.head
            while (p != p-1):
                temp = temp.next
                p +=1
            new_node.next = temp.next
            temp.next = new_node

    # deleting the value

    def delete(self, value):
        temp=self.head
        prev=None
        if temp.data==value:
            elf.head=self.head.next
        else:
            while(temp.data!=value and temp):
                prev=temp
                temp=temp.next
                if temp==None:
                    print("Value is not present in the list")
                    return 
            prev.next=temp.next
            temp=None
    

    # 

    def middle(self):
        slow = self.head
        fast = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        if slow:
            print("Middle node:", slow.data)

        

    def display(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next
        

        


list1=SLL()
n1 = Node(10)
n2 = Node(20)

list1.insert(n1)
list1.insert(n2)
list1.insert(Node(30))
list1.insert(Node(40))


list1.append(Node(60),1)


list1.delete(10)






    # list1.append((60), 1)


list1.display()

list1.middle()