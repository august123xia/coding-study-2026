def lower_bound(nums, target):
    left = 0 
    right = len(nums) - 1

    while left <= right :
        mid = (left + right) // 2

        if nums[mid] >= target:
            right = mid - 1

        else:
            left = mid + 1

    return left

print(lower_bound([1, 3, 5, 6], 2))  # 1
print(lower_bound([1, 3, 5, 6], 5))  # 2
print(lower_bound([1, 3, 5, 6], 7))  # 4
print(lower_bound([1, 3, 5, 6], 0))  # 0

# Review:
# Lower bound means finding the first index where nums[index] >= target.
# Binary search can be used not only to find an exact target, but also to find a boundary.
# If nums[mid] >= target, move right to mid - 1 because we want to search further left.
# If nums[mid] < target, move left to mid + 1 because the answer must be on the right.
# When the loop ends, left is the first valid position.
# mid = (left + right) // 2 needs parentheses.
# left == right means one element is still left to check, so we use while left <= right.