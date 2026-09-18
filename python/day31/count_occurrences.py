def lower_bound(nums, target):
    left = 0 
    right = len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] >= target:
            right = mid -1
        else:
            left = mid + 1

    return left

def upper_bound(nums, target):
    left = 0 
    right = len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] > target:
            right = mid -1
        else:
            left = mid + 1

    return left

def count_occurrences(nums, target):
    count = upper_bound(nums, target) - lower_bound(nums, target)
    return count

print(count_occurrences([1, 2, 2, 2, 3, 4], 2))  # 3
print(count_occurrences([1, 2, 2, 2, 3, 4], 3))  # 1
print(count_occurrences([1, 2, 2, 2, 3, 4], 5))  # 0
print(count_occurrences([], 2))                  # 0


def contains_target(nums, target):
    pos = lower_bound(nums, target)

    if pos == len(nums):
        return False
    
    elif nums[pos] != target:
        return False
    
    else:
        return True
    
print(contains_target([1, 2, 2, 2, 3, 4], 2))  # True
print(contains_target([1, 2, 2, 2, 3, 4], 5))  # False
print(contains_target([], 2))                  # False