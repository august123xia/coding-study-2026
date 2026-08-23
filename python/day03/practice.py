def contain_duplicate(nums):
    seen = set()

    for i in nums:
        if i in seen:
            return True
        
        seen.add(i)

    return False

nums = [4, 1, 6, 4]
answer = contain_duplicate(nums)
print (answer)