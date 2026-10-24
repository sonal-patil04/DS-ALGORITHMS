# sum of cube of natural numbers

# if we have number 4
# the execution will be 
# 8=cube of 1+cube of 2 + cube of 3 +----------+cube of 8



sum=0
n=int(input("Enter a number : "))

sum=((n*(n+1))//2)**2
print("sum is : ",sum)