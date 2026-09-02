def majority_element(nums):
    seen = {}
    for num in nums:
        if num in seen:
            seen[num] += 1
        else:
            seen[num] = 1
        
        if  seen[num] > (len(nums) / 2):
            return num

nums = [2, 2, 1, 1, 1, 2, 2]
print(majority_element(nums))

print(majority_element([3, 2, 3]))              # 3
print(majority_element([2, 2, 1, 1, 1, 2, 2]))  # 2

# Review:
# This solution uses a dictionary to count how many times each number appears.
# The key is the number, and the value is its count.
# If a number appears more than len(nums) / 2 times, it is the majority element.
# return ends the whole function, not just the loop.
# This is similar to Valid Anagram, but we count numbers instead of characters.