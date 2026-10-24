# 2. Find the smallest and Largest Element: Write a program to accept N integers into an array and find and display the largest element, second largest element, smallest element, second smallest element present in the array. 

n = int(input("Enter the number of elements: "))

arr = []

for i in range(n):
    num = int(input("Enter element: "))
    arr.append(num)

print(arr)

# arr.sort()
smallest=arr[0]
largest=arr[0]
sec_smallest=arr[0]
sec_largest=arr[0]


for i in arr:
    if (i<smallest):
        sec_smallest=smallest
        smallest=i

for i in arr:
    if (i>largest):
        sec_largest=largest
        largest=i

print(arr)

# print(arr[0])
print("Smallest : ", smallest)
print("Largest: ",largest)
print("Second Smallest : ", sec_smallest)
print("Second Largest: ",sec_largest)



     

# -------------------------------------------------------------


# n = int(input("Enter the number of elements: "))

# arr = []

# for i in range(n):
#     num = int(input("Enter element: "))
#     arr.append(num)

# arr.sort()

# print("Smallest element:", arr[0])
# print("Second smallest element:", arr[1])
# print("Second largest element:", arr[-2])
# print("Largest element:", arr[-1])