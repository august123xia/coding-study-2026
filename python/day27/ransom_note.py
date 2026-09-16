def can_construct(ransomNote, magazine):
    count = {}
    for char in magazine:
        if char in count:
            count[char] += 1
        else:
            count[char] =1
    
    for char in ransomNote:
        if char not in count or count[char] == 0:
            return False
            
        count[char] -= 1
    
    return True
        

print(can_construct("aa", "aab"))  # True
print(can_construct("aa", "ab"))   # False
print(can_construct("a", "b"))     # False
print(can_construct("", "abc"))    # True

# Review:
# Use a dictionary to count available characters in magazine.
# ransomNote is the demand.
# magazine is the inventory.
# If a required character is missing or used up, return False.
# Otherwise, use one character by doing count[char] -= 1.
# If all required characters are available, return True.