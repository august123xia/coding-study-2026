def two_sum(nums, target):
    # your code here
    seen = {}

    for i , num in enumerate(nums):
        complement = target - num

        if complement in seen:
            return[seen[complement], i]
        
        else:
            seen[num]=i

nums = [3, 2, 4]
target = 6

print(two_sum(nums, target))