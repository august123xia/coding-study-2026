def remove_element(nums, val):
    write_pos = 0
    for num in nums:
        if num != val:
            nums[write_pos]=num
            write_pos += 1
    return write_pos

nums = [3, 2, 2, 3]
k = remove_element(nums, 3)
print(k)
print(nums[:k])

nums = [0, 1, 2, 2, 3, 0, 4, 2]
k = remove_element(nums, 2)
print(k)
print(nums[:k])
