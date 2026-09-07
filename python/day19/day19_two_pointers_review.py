def reverse_string(s):
    chars = list(s)

    left = 0
    right = len(chars) - 1

    while left < right:
        pos = chars[left]
        chars[left] = chars[right]
        chars[right] = pos

        left += 1
        right -= 1


    return "".join(chars)


print(reverse_string("hello"))    # olleh
print(reverse_string("abc"))      # cba
print(reverse_string("racecar"))  # racecar
