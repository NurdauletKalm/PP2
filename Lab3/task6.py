from itertools import permutations

def solve(s):
    perm = permutations(s)
    
    for p in perm:
        print(''.join(p))
        
s = input()
solve(s)