def count_letters(word):
    # your code here
    count ={}

    for char in  word:
        if char in count:
            count[char] += 1
        else:  
            count[char] = 1
    
    return count


def is_anagram(s, t):
    # your code here
    return count_letters(s) == count_letters(t)


print(is_anagram("listen", "silent"))