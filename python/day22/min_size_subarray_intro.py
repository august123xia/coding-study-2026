nums = [2, 3, 1, 2, 4, 3]
target = 7

left = 0
window_sum = 0

for right in range(len(nums)):
    window_sum += nums[right]
    print("add:", nums[right], "window_sum:", window_sum)

    while window_sum >= target:
        print("valid window:", nums[left:right + 1], "length:", right - left + 1)

        window_sum -= nums[left]
        left += 1