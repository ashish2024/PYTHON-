"""n=int(input())
t=n

r=0
while(n>0):
    d=n%10
    r=r*10+d
    n=n//10
if(r==t):
    print("Palindrome")
else:
    print("Not a Palindrome")"""
# type 2 
"""n=input()
t=n
if t==n[::-1]:
     print("Palindrome")
else:
    print("Not a Palindrome")
"""
# type 3
"""
n=int(input())
t=n
k=int(str(n)[::-1])
if t==k:
    print("Palindrome")
else:
    print("Not a Palindrome")
"""# type 4 using recursion 
"""def ispalindrome(n,t,r=0):
    

    if n==0:
        if t==r:
            return "Palindorme"
        else:
            return "Not a palindrome"
    else:
        while(n>0):
            d=n%10
            r=r*10+d
            n=n//10
            return ispalindrome(n,t)
        
n = int(input("Enter number:"))
result = ispalindrome(n, n)
print(result)
"""
"""
def checkpalindrome(str):
    l=len(str)
    m=int(l/2)
    for i in range(m):
        if str[i]!=str[l-i-1]:
            return False
        return True
str=input("ENtre the no::")
if checkpalindrome(str):
    print("Palindrome")
else:
    print("Not a palindrome")"""
def checkpalindrome(n):
    return str(n) == ''.join(reversed(str(n)))
    
    

n=input()

if checkpalindrome(n):
    print("Palindrome")
else:
    print("Not a palindrome")






