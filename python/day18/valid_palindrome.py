def is_palindrome(s):
    left = 0
    right = len(s) - 1

    while left < right:
        if not s[left].isalnum():
            left += 1
            continue

        if not s[right].isalnum():
            right -= 1
            continue

        if s[left].lower() != s[right].lower():
            return False

        # move both pointers here
        left += 1
        right -= 1

    return True


print(is_palindrome("A man, a plan, a canal: Panama"))  # True
print(is_palindrome("race a car"))                       # False
print(is_palindrome(" "))                                # True

# Review:
# Two pointers means using left and right to scan from both sides.
# while left < right means we keep checking until the two pointers meet.
# isalnum() checks whether a character is a letter or number.
# not isalnum() means the character should be skipped.
# continue skips the rest of the current loop and starts the next loop.
# lower() is used to compare characters without caring about uppercase or lowercase.
# return False means we found a mismatch.
# return True means all valid characters matched.