
# Binary Search Tree

class Node:
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, new_node):
        if self.root is None:
            self.root = new_node
        else:
            temp = self.root

            while True:
                if new_node.data < temp.data:
                    if temp.left is None:
                        temp.left = new_node
                        return
                    else:
                        temp = temp.left

                else:
                    if temp.right is None:
                        temp.right = new_node
                        return
                    else:
                        temp = temp.right

    # Delete node
    def del_node(self, rt, val):
        if rt is None:
            return rt

        if val < rt.data:
            rt.left = self.del_node(rt.left, val)

        elif val > rt.data:
            rt.right = self.del_node(rt.right, val)

        else:
            # Case 1: No left child
            if rt.left is None:
                return rt.right

            # Case 2: No right child
            if rt.right is None:
                return rt.left

            # Case 3: Both children exist
            succ = self.get_successor(rt)
            rt.data = succ.data
            rt.right = self.del_node(rt.right, succ.data)

        return rt

    # Find inorder successor
    def get_successor(self, temp):
        temp = temp.right

        while temp is not None and temp.left is not None:
            temp = temp.left

        return temp

    # Inorder: Left Root Right
    def inorder(self, rt):
        if rt is None:
            return
        self.inorder(rt.left)
        print(rt.data, end=" ")
        self.inorder(rt.right)

    # Preorder: Root Left Right
    def preorder(self, rt):
        if rt is None:
            return
        print(rt.data, end=" ")
        self.preorder(rt.left)
        self.preorder(rt.right)

    # Postorder: Left Right Root
    def postorder(self, rt):
        if rt is None:
            return
        self.postorder(rt.left)
        self.postorder(rt.right)
        print(rt.data, end=" ")

    # Find minimum and maximum
    def findminmax(self):
        if self.root is None:
            print("Tree is empty")
            return

        temp = self.root
        while temp.left:
            temp = temp.left
        print("\nMin:", temp.data)

        temp = self.root
        while temp.right:
            temp = temp.right
        print("Max:", temp.data)


# Main program

b1 = BST()

b1.insert(Node(100))
b1.insert(Node(10))
b1.insert(Node(450))
b1.insert(Node(4))
b1.insert(Node(65))
b1.insert(Node(300))
b1.insert(Node(500))

print("Inorder:")
b1.inorder(b1.root)

print("\n\nPreorder:")
b1.preorder(b1.root)

print("\n\nPostorder:")
b1.postorder(b1.root)

b1.findminmax()

# Delete node
b1.root = b1.del_node(b1.root, 65)

print("\n\nAfter delete:")
b1.inorder(b1.root)
