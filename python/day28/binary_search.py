def search(nums, target):
    left = 0
    right = len(nums) -1

    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        
        elif nums[mid] > target:
            right = mid -1

        else: 
            left = mid + 1

    return -1

print(search([1, 3, 5, 7, 9, 11], 7))   # 3
print(search([1, 3, 5, 7, 9, 11], 1))   # 0
print(search([1, 3, 5, 7, 9, 11], 11))  # 5
print(search([1, 3, 5, 7, 9, 11], 6))   # -1


# Review:
# Binary search works on a sorted array.
# left and right define the current search range.
# mid is the middle index of the current range.
# If nums[mid] is too large, move right to mid - 1.
# If nums[mid] is too small, move left to mid + 1.
# If the target is found, return its index.
# If the loop ends without finding the target, return -1.