s = "([])"

stack = []

pairs = {
    ")": "(",
    "]": "[",
    "}": "{"
}

for char in s:
    print("checking:", char)

    if char in pairs.values():
        stack.append(char)
        print("push:", stack)

    elif char in pairs:
        top = stack.pop()
        print("pop:", top)

        if top != pairs[char]:
            print("not valid")
            break

print("final stack:", stack)

# Review:
# pairs is a dictionary.
# In this dictionary, right brackets are keys and left brackets are values.
# char in pairs checks whether char is a right bracket.
# char in pairs.values() checks whether char is a left bracket.
# Stack stores left brackets that have not been matched yet.
# When we see a right bracket, we pop the latest left bracket and check if they match.