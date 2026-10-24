# palindrome

num=int(input("Enter a number : "))
sum=0
n=num

while(num>0):
    sum=sum*10+(num%10)
    num=num//10
if (n==sum):
    print("The given number is palindrome")
else:
    print("The given number is not palindrome")