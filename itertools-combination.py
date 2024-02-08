from itertools import combinations
s , l  = input().split()
for i in range(1, int(l)+1):
    for j in combinations(sorted(s), i):
        print (''.join(j))
