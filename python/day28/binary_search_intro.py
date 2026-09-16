nums = [1, 3, 5, 7, 9, 11]
target = 7

left = 0
right = len(nums) - 1

while left <= right:
    mid = (left + right) // 2

    print("left:", left, "right:", right, "mid:", mid, "value:", nums[mid])

    if nums[mid] == target:
        print("found index:", mid)
        break
    elif nums[mid] < target:
        left = mid + 1
    else:
        right = mid - 1