def remove_duplicates_sorted(nums):
    if len(nums) == 0:
       return []
    
    write_pros = 0
    for num in nums:
        if num != nums[write_pros]:
            write_pros += 1
            nums[write_pros] = num
    return nums[:write_pros + 1]

print(remove_duplicates_sorted([1, 1, 2]))              # [1, 2]
print(remove_duplicates_sorted([1, 1, 2, 2, 3, 3, 4]))  # [1, 2, 3, 4]
print(remove_duplicates_sorted([1, 2, 3]))              # [1, 2, 3]
print(remove_duplicates_sorted([]))                     # []