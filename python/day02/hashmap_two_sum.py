def two_sum(nums, target):
    seen = {}

    for i, num in enumerate(nums):
        complement = target  - num
    
        print("i:", i, "num:", num, "complement:", complement, "seen:", seen)
    
        if complement in seen:
            return [seen[complement], i]
        

        seen[num] = i

nums = [5, 1, 9, 4]
target = 10

answer = two_sum(nums, target)
print(answer)