nums = [1, 3, 5, 6]
target = 2

left = 0
right = len(nums) - 1

while left <= right:
    mid = (left + right) // 2

    print("left:", left, "right:", right, "mid:", mid, "value:", nums[mid])

    if nums[mid] >= target:
        right = mid - 1
    else:
        left = mid + 1

print("insert position:", left)