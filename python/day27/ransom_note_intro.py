magazine = "aab"
ransomNote = "aa"

count = {}

for char in magazine:
    if char in count:
        count[char] += 1
    else:
        count[char] = 1

print(count)

for char in ransomNote:
    print("need:", char)

    if char not in count or count[char] == 0:
        print("cannot build")
        break

    count[char] -= 1
    print("use one:", char, count)