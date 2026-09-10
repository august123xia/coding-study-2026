def find_max_average(nums, k):
    total = sum(nums[:k])
    max_total = total
    for i in range(k, len(nums)):
        total = total - nums[i-k]+ nums[i]
        if total > max_total:
            max_total = total

    return max_total/k

print(find_max_average([1, 12, -5, -6, 50, 3], 4))  # 12.75
print(find_max_average([5], 1))                      # 5.0
print(find_max_average([2, 1, 5, 1, 3, 2], 3))       # 3.0
print(find_max_average([10, 20, 30, 40], 2))         # 35.0