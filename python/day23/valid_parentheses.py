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