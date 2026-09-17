def search_insert(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left +  right) //  2
        if nums[mid] == target:
            return mid
        
        elif nums[mid] > target:
            right = mid -1

        else: 
            left = mid + 1

    return left

print(search_insert([1, 3, 5, 6], 5))  # 2
print(search_insert([1, 3, 5, 6], 2))  # 1
print(search_insert([1, 3, 5, 6], 7))  # 4
print(search_insert([1, 3, 5, 6], 0))  # 0


# Review:
# Search Insert Position uses the binary search pattern.
# If nums[mid] equals target, return mid.
# If nums[mid] is too large, move right to mid - 1.
# If nums[mid] is too small, move left to mid + 1.
# If the target is not found, left becomes the correct insert position.