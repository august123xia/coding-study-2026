def min_sub_array_len(target, nums):
    left = 0
    window_sum = 0
    min_length = len(nums) + 1

    for right in range(len(nums)):
        window_sum += nums[right]

        while window_sum >= target:
            current_length = right - left + 1

            if current_length < min_length:
                min_length = current_length

            window_sum -= nums[left]
            left += 1

    if min_length == len(nums) + 1:
        return 0

    return min_length


print(min_sub_array_len(7, [2, 3, 1, 2, 4, 3]))  # 2
print(min_sub_array_len(4, [1, 4, 4]))            # 1
print(min_sub_array_len(11, [1, 1, 1, 1, 1]))     # 0

# Review:
# Fixed-size sliding window has a fixed window length k.
# Variable-size sliding window changes the window length.
# right expands the window by adding new numbers.
# left shrinks the window when the window_sum is large enough.
# We use while instead of if because the window may need to shrink multiple times.
# current_length = right - left + 1 because both left and right are included.

#We use while instaed of if because after fixing the right boundary,
#the left boundary may need to move multiple times while the window is still valid.
#this helps us find the shortest valid window