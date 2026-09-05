nums = [1, 1, 2, 2, 3, 3, 4]

for i, num in enumerate(nums):
    print(i, num)
    i += 1

print(nums[-1])
print(nums[:3])

def remove_duplicates_sorted(nums):
    result = []
    for num in nums:
        if len(result) == 0 or num != result[-1]:
            result.append(num)
    
    return result

print(remove_duplicates_sorted(nums))
print(remove_duplicates_sorted([1, 1, 2]))
print(remove_duplicates_sorted([1, 2, 3]))
print(remove_duplicates_sorted([]))