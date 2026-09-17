def lower_bound(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] >= target:
            right = mid - 1
        else:
            left = mid + 1

    return left


def upper_bound(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] > target:
            right = mid - 1
        else:
            left = mid + 1

    return left

def search_range(nums, target):
    first = lower_bound(nums, target)
    if first == len(nums) or nums[first] != target:
        return [-1, -1]
    last = upper_bound(nums, target) - 1
    return [first, last]

print(search_range([1, 2, 2, 2, 3, 4], 2))  # [1, 3]
print(search_range([1, 2, 2, 2, 3, 4], 3))  # [4, 4]
print(search_range([1, 2, 2, 2, 3, 4], 5))  # [-1, -1]
print(search_range([], 2))                  # [-1, -1]

# Review:
# lower_bound finds the first index where nums[index] >= target.
# upper_bound finds the first index where nums[index] > target.
# The first position of target is lower_bound(nums, target).
# The last position of target is upper_bound(nums, target) - 1.
# If first == len(nums), target does not exist.
# If nums[first] != target, target does not exist.
# When target does not exist, return [-1, -1].