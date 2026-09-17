nums = [1, 2, 2, 2, 3, 4]
target = 2

left = 0
right = len(nums) - 1

while left <= right:
    mid = (left + right) // 2

    print("left:", left, "right:", right, "mid:", mid, "value:", nums[mid])

    if nums[mid] > target:
        right = mid - 1
    else:
        left = mid + 1

print("upper bound position:", left)