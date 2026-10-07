# 3. Count Even and Odd Numbers: Write a program to accept N integers into an array and count and display the number of even and odd elements present in the array. 

n = int(input("Enter the number of elements: "))

arr = []

for i in range(n):
    num = int(input("Enter element: "))
    arr.append(num)

# print(arr)



count_even=0
count_odd=0


for i in arr:
    if i%2==0:
        count_even+=1
        # print("Even: ",i)

    else:
        count_odd+=1
        # print("Odd ",i)

print()


print("Even: ",count_even)
print("Odd: ",count_odd)


