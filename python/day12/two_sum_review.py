nums = [2, 7, 11, 15]
target = 9

def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num

        if complement in seen:
            return [seen[complement], i]
        
        seen[num]=i

        
print(two_sum(nums, target))

# Review:
# seen stores numbers we have already visited and their indexes.
# complement means the number needed to reach the target.
# If complement is already in seen, we found the answer.
# Return [seen[complement], i] because the problem asks for indexes.  