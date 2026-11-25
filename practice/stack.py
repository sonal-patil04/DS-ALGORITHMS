# Q. 1 Create a Stack with following operations
# 1. Push
# 2. Pop
# 3. Display
# 4. Reverse String using Stack
# 5. Reverse Stack using another Stack

class stack():
    def __init__(self):
        self.values=[]

    def push(self,x):
        self.values+=[x]

    def pop(self):
        if len(self.values)==0:
            print("Stack is empty")
        else:
            return self.values.pop()

    def display(self):
        print(self.values)

    
    def reverse_stack(self):
        # rev_stack=[]
        # while len(self.values)>0:
        #    rev_stack.append(self.values.pop())
        # return rev_stack
        # return self.values.pop()

        s2=stack()
        while len(self.values)>0:
            s2.push(self.pop())
        return s2.values


s=stack()
s.push(10)
s.push(20)
s.push(30)

print("original stack----->")
s.display()

s.pop()
# s.pop()
# s.pop()
# s.pop()

print()
print("stack after pop-->")
s.display()

print()
print("reverse stack--->")
print(s.reverse_stack())
# print(s.values[::-1])

def reverse_str(string):
    s=stack()
    for ch in string:
        s.push(ch)

    result=""
    while len(s.values)>0:
        result+=s.pop()
    return result

print()
text="hello"
print("original string-->",text)
print("reversed string--->",reverse_str(text))