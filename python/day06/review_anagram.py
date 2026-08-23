def count_letters(word):
    seen = {}
    for i in word:
        if i in seen:
           seen [i] = seen[i] + 1
        else:
            seen[i] = 1
    return seen


def is_anagram(s, t):
    return count_letters(s) == count_letters(t)

s = "listen"
t = "silent"

answer = is_anagram(s, t)
print(answer)