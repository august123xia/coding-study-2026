nums = [3, 2, 2, 3]
val = 3

write_pos = 0

for num in nums:
    print("checking:", num)

    if num != val:
        nums[write_pos] = num
        write_pos += 1
        print("keep:", nums, "write_pos:", write_pos)
    else:
        print("remove:", num)

print(nums)
print(write_pos)
print(nums[:write_pos])


def remove_element(nums, val):
    write_pos = 0

    for num in nums:
        if num != val:
            nums[write_pos] = num
            write_pos += 1
        
    return write_pos

nums = [3, 2, 2, 3]
k = remove_element(nums, 3)
print(k)          # 2
print(nums[:k])   # [2, 2]

nums = [0, 1, 2, 2, 3, 0, 4, 2]
k = remove_element(nums, 2)
print(k)          # 5
print(nums[:k])   # [0, 1, 3, 0, 4]

# Review:
# Remove Element uses the in-place overwrite pattern.
# write_pos means the next position for a value we want to keep.
# If num != val, we keep it by writing it to nums[write_pos].
# Then write_pos moves one step forward.
# return write_pos gives the number of remaining valid elements.
# nums[:write_pos] shows the valid part of the list.