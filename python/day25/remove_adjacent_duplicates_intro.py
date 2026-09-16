s = "abbaca"

stack = []

for char in s:
    print("checking:", char)

    if len(stack) > 0 and stack[-1] == char:
        removed = stack.pop()
        print("pop:", removed, stack)
    else:
        stack.append(char)
        print("push:", stack)

print("final stack:", stack)
print("result:", "".join(stack))