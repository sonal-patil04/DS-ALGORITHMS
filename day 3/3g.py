# 7. Move Zeros to the End: Write a program to accept N integers into an array
#  and rearrange the elements so that all 0 values are moved to the end while
# maintaining the relative order of the non-zero elements.


n=int(input("Enter number of elements: "))

arr=[]

for i in range(n):
    num=int(input("Enter element: "))
    arr.append(num)

print(arr)

new_arr=[]

for i in arr:
    if i!=0:
        new_arr.append(i)

for i in arr:
    if i==0:
        new_arr.append(i)

print(new_arr)