# 6. Remove Duplicate Elements: Write a program to accept N integers into an 
# array and create a new array containing only the unique elements, removing 
# all duplicate values. 

n = int (input("Enter the size of array (n) :"))
arr =[]
for i in range (0,n,+1):
    a = int (input("Enter the element of array :"))
    arr.append(a)
print(arr)

is_present = False
num = int(input("enter number to search : "))
p_index = 0
for j in range(0,len(arr)-1) :
    for i in arr :
        if i == num :
            is_present = True
            p_index = j

if is_present :
    print(f"number is present in the array at position {p_index}")
else :
    print("number is not present in the array")