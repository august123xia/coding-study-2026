def max_sum_subarray_optimized(nums, k):
    window_sum = sum(nums[:k])
    max_sum = window_sum

    for i in range(k, len(nums)):
        window_sum = window_sum - nums[i - k] + nums[i]

        if window_sum > max_sum:
            max_sum = window_sum

    return max_sum


print(max_sum_subarray_optimized([1, 3, 2, 5, 4, 8], 3))  # 17
print(max_sum_subarray_optimized([2, 1, 5, 1, 3, 2], 3))  # 9
print(max_sum_subarray_optimized([5, 5, 5], 2))           # 10

# Review:
# Sliding window means keeping a fixed-size window and moving it to the right.
# window_sum stores the current window total.
# nums[i - k] is the number leaving the window.
# nums[i] is the number entering the window.
# New window sum = old window sum - outgoing number + incoming number.
# This is faster than recalculating sum(window) every time.