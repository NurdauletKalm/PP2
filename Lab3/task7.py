def has_33(a):
    ok = False
    for i in range(len(a) - 1):
        if a[i] == 3 and a[i + 1] == 3:
            return True
    return False
nums = list(map(int, input().split()))
print(has_33(nums))