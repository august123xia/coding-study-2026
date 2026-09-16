def is_valid(s):
    stack = []

    pairs = {
        ")": "(",
        "]": "[",
        "}": "{"
    }

    for char in s:
        if char in pairs.values():
            stack.append(char)
            pass

        elif char in pairs:
            # if no left bracket to match
            if len(stack) == 0:
                return False


            # pop and check
            top = stack.pop()
            if top != pairs[char]:
                return False


    # final check
    return len(stack) == 0


print(is_valid("()"))        # True
print(is_valid("()[]{}"))    # True
print(is_valid("(]"))        # False
print(is_valid("([)]"))      # False
print(is_valid("([])"))      # True
print(is_valid("("))         # False
print(is_valid(")"))         # False

# Review:
# Stack follows Last In, First Out.
# In this problem, stack stores left brackets that have not been matched.
# pairs is a dictionary where right brackets are keys and left brackets are values.
# char in pairs checks whether char is a right bracket.
# char in pairs.values() checks whether char is a left bracket.
# When we see a right bracket, we pop the latest left bracket and check if it matches.
# return len(stack) == 0 means the string is valid only if all left brackets are matched.