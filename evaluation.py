
class Node:
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None


class BST:

    def __init__(self):
        self.root = None
        self.cnt = 0
        self.total = 0

    # Insert node
    def insert(self, new_node):
        if self.root is None:
            self.root = new_node
            return

        temp = self.root
        while True:
            if new_node.data < temp.data:
                if temp.left is None:
                    temp.left = new_node
                    return
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                    return
                temp = temp.right

    # Display scores in ascending order
    def inorder(self, rt):
        if rt is None:
            return

        self.inorder(rt.left)
        print(rt.data, end=" ")
        self.inorder(rt.right)

    # Find minimum and maximum
    def findminmax(self):
        if self.root is None:
            print("BST is empty")
            return

        temp = self.root
        while temp.left is not None:
            temp = temp.left
        print("Lowest score:", temp.data)

        temp = self.root
        while temp.right is not None:
            temp = temp.right
        print("Highest score:", temp.data)

    # Count students scoring above 50
    def count_above_50(self, rt):
        if rt is None:
            return 0

        count = 0
        if rt.data > 50:
            count = 1

        return (count
                + self.count_above_50(rt.left)
                + self.count_above_50(rt.right))

    # Search for a particular score
    def search(self, key):
        temp = self.root

        while temp is not None:
            if temp.data == key:
                return True
            elif key < temp.data:
                temp = temp.left
            else:
                temp = temp.right

        return False

    # Calculate average of all scores
    def calculate_average(self, rt):
        if rt is None:
            return

        self.calculate_average(rt.left)
        self.total += rt.data
        self.cnt += 1
        self.calculate_average(rt.right)

    def average(self):
        self.cnt = 0
        self.total = 0

        self.calculate_average(self.root)

        if self.cnt == 0:
            print("BST is empty")
        else:
            print("Average score:", self.total / self.cnt)


# Driver Code

b1 = BST()

scores = [45, 78, 32, 89, 56, 92,
          67, 34, 85, 73, 61, 98]

for val in scores:
    b1.insert(Node(val))


print("Scores in ascending order:")
b1.inorder(b1.root)

print("\nLowest and highest scores:")
b1.findminmax()

print("\nNumber of students scoring above 50:",
      b1.count_above_50(b1.root))

key = 67

if b1.search(key):
    print("Score", key, "found")
else:
    print("Score", key, "not found")

print()
b1.average()
