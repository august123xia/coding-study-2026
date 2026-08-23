word = "apple"

count = {}

for char in word:
    if char in count:
        count[char] = count[char] + 1
    else:
        count[char] = 1

print(count)