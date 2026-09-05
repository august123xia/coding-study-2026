s = "racecar"

left = 0
right = len(s) - 1

while left < right:
    print(left, right, s[left], s[right])
    left += 1
    right -= 1