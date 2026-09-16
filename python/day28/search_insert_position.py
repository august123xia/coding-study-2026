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