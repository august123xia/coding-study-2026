def remove_duplicates_sorted(nums):
    result = []
    for num in nums:
        if len(result) == 0 or num != result[-1]:
            result.append(num)
    return result

print(remove_duplicates_sorted([1, 1, 2]))              # [1, 2]
print(remove_duplicates_sorted([1, 1, 2, 2, 3, 3, 4]))  # [1, 2, 3, 4]
print(remove_duplicates_sorted([1, 2, 3]))              # [1, 2, 3]
print(remove_duplicates_sorted([]))                     # []

# Review:
# This solution removes duplicates from a sorted list.
# result stores the unique numbers.
# result[-1] means the last value in result.
# If result is empty, we append the first number.
# If the current number is different from result[-1], we append it.
# The condition uses "or" to handle the empty result case safely.