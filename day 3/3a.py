# 1. Calculate Array Sum: 
# Write a program to accept N integers into an array and calculate and display the sum of all the elements. 



n=int(input("Enter number of elements: "))
arr=[]

for i in range(n):
    num=int(input("Enter a number: "))
    arr.append(num)

# print(arr)

sum=0

for i in arr:
    sum=sum+i

print("sum of all elements is: ",sum)