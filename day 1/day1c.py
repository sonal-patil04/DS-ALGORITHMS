# Create array, find second min & second max

arr=[10,40,56,2,6,3,6,34,98,45]
min=arr[0]
max=arr[0]

for num in arr:
    if num<min:
        smin=num             #this logic will only work for sorted array
        min=num
    if num>max:
        smax=num
        max=num
        
print("Minimum: ",min)
print("Maximum: ",max)

print("Second Minimum: ",smin)
print("Second Maximum: ",smax)

