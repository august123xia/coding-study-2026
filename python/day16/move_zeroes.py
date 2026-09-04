def move_zeroes(nums):
    insert_pos = 0

    for num in nums:
        if num != 0:
            nums[insert_pos] = num
            insert_pos += 1

    for i in range(insert_pos, len(nums)):
        nums[i] = 0

    return nums


print(move_zeroes([0, 1, 0, 3, 12]))  # [1, 3, 12, 0, 0]
print(move_zeroes([0, 0, 1]))         # [1, 0, 0]
print(move_zeroes([1, 2, 3]))         # [1, 2, 3]

# Review:
# Simple version: create a new list for non-zero numbers, then append zeros.
# In-place version: modify the original nums list directly.
# insert_pos means the next position for a non-zero number.
# First, move all non-zero numbers to the front.
# Then, fill the remaining positions with zeros.
# return nums is used here so we can print and test the result.