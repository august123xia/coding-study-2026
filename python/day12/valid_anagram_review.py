def count_letters(word):
    seen = {}
    for char in word:
        if char in seen:
            seen[char] += 1
        else:
            seen[char]=1

    
    return seen

def is_anagram(s, t):
    if count_letters(s) == count_letters(t):
        return True
    
    else:
        return False

print(is_anagram("anagram", "nagaram"))  # True
print(is_anagram("rat", "car"))          # False

# Review:
# count_letters() uses a dict to count how many times each character appears.
# if decides which branch to enter.
# return sends the result back from the function.
# We can return True or False explicitly.