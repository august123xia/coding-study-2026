def contains_duplicate(nums):
    # your code here
    seen = set()
    
    for num in nums:
        if num in seen:
            return True
        else:
            seen.add(num)
    
    return False

nums = [1, 2, 3, 1]
print(contains_duplicate(nums))