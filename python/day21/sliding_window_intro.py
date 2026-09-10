def max_sum_subarray(nums, k):
    windows=[]
    max_sum = 0
    for i in range(0, len(nums)-k+1):
         windows=nums[i:i+k]
         total_sum=sum(windows)
         if total_sum > max_sum:
              max_sum = total_sum
    
    return max_sum
              
print(max_sum_subarray([1, 3, 2, 5, 4, 8], 3))  # 17
print(max_sum_subarray([2, 1, 5, 1, 3, 2], 3))  # 9



        
    