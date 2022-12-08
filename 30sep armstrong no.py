# wap to check the given no is armstrong or not

n=input("Enter a number: ")
l=len(n)
s=0
for i in range(0,l):
    s+=int(n[i])**l
print("Sum of Digits:",s)
if(s==int(n)):
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")
