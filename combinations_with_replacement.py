# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations_with_replacement
s , l  = input().split()
for j in combinations_with_replacement(sorted(s), int(l)):
    print (''.join(j))
