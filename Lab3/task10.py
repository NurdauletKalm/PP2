def solve(a):
    ans = []
    for i in a:
        if i not in ans:
            ans.append(i)
    return ans

a = input().split()
print(solve(a))