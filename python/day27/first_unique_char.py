def first_unique_char(s):
    count = {}
    for char in s:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1

    for i, char in enumerate(s):
        if count[char] == 1:
            return i
        
    return -1

print(first_unique_char("leetcode"))      # 0
print(first_unique_char("loveleetcode"))  # 2
print(first_unique_char("aabb"))          # -1
print(first_unique_char("a"))             # 0

# Review:
# Use a dictionary to count how many times each character appears.
# The first loop builds the frequency map.
# The second loop checks characters from left to right.
# If count[char] == 1, return its index immediately.
# If no unique character exists, return -1.
