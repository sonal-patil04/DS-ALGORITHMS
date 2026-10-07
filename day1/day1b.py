# Create array, find min max

arr=[10,40,56,2,6,3,6,34,98,45]
min=arr[0]
max=arr[0]

for num in arr:
    if num<min:
        min=num
    if num>max:
        max=num

        
print("Minimum: ",min)
print("Maximum: ",max)
