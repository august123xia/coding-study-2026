s = "leetcode"

count = {}

for char in s:
    if char in count:
        count[char] += 1
    else:
        count[char] = 1

print(count)

for i, char in enumerate(s):
    print(i, char, count[char])

    if count[char] == 1:
        print("first unique index:", i)
        break