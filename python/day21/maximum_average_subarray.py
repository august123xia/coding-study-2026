def find_max_average(nums, k):
    window_sum = sum(nums[:k])
    max_sum = window_sum
    for i in range(k,len(nums)):
        window_sum = window_sum - nums[i-k] + nums[i] 
        if window_sum > max_sum:
            max_sum = window_sum
    
    return max_sum/k

print(find_max_average([1, 12, -5, -6, 50, 3], 4))  # 12.75
print(find_max_average([5], 1))                      # 5.0
print(find_max_average([2, 1, 5, 1, 3, 2], 3))       # 3.0