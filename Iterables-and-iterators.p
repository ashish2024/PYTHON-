# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations
t = int(input())
s=list(input().split())
k= int(input())
l1=list(combinations(s,k))
r=[]
for i in l1:
    if 'a' in i:
        r.append(i)
        
print(len(r)/len(l1))
        

        

   
    
