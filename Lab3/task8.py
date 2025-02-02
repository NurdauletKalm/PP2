def oo7(nums):
    ok = False
    for i in range(len(nums)):
        if nums[i] == 0 and nums[i + 1] == 0 and nums[i + 2] == 7:
            return True
    return False        
nums = list(map(int, input().split()))
print(oo7(nums))