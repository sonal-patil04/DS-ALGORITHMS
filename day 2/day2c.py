# Armstrong

num=eval(input("Enter a number : "))
p=len(str(num))
sum=0
n=num
while(num>0):
    sum+=(num%10)**p
    num//=10
if (n==sum):
    print("the given number is armstrong")
else:
    print("the given number is not armstrong")