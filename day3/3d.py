# # 4. Search an Element: Write a program to accept N integers into an array and search for a given number. Display an appropriate message indicating whether the number is present in the array or not and also display its position. 




n = int(input("Enter the number of elements: "))

arr = []

for i in range(n):
    num = int(input("Enter element: "))
    arr.append(num)

print(arr)

search = int(input("Enter the number to search: "))

found = False

for i in range(n):
    if arr[i] == search:
        print("Element found at position: ", i+1)
        found = True

if found == False:
    print("Element not found")