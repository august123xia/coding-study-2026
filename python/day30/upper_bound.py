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


print(upper_bound([1, 2, 2, 2, 3, 4], 2))  # 4
print(upper_bound([1, 2, 2, 2, 3, 4], 1))  # 1
print(upper_bound([1, 2, 2, 2, 3, 4], 4))  # 6
print(upper_bound([1, 2, 2, 2, 3, 4], 0))  # 0