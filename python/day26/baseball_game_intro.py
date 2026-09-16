ops = ["5", "2", "C", "D", "+"]

stack = []

for op in ops:
    print("checking:", op)

    if op == "C":
        removed = stack.pop()
        print("cancel:", removed, stack)

    elif op == "D":
        new_score = stack[-1] * 2
        stack.append(new_score)
        print("double:", new_score, stack)

    elif op == "+":
        new_score = stack[-1] + stack[-2]
        stack.append(new_score)
        print("sum last two:", new_score, stack)

    else:
        stack.append(int(op))
        print("add score:", stack)

print("final stack:", stack)
print("total:", sum(stack))

ops = ["5", "2", "C", "D", "+"]

stack = []

for op in ops:
    print("checking:", op)

    if op == "C":
        removed = stack.pop()
        print("cancel:", removed, stack)

    elif op == "D":
        new_score = stack[-1] * 2
        stack.append(new_score)
        print("double:", new_score, stack)

    elif op == "+":
        new_score = stack[-1] + stack[-2]
        stack.append(new_score)
        print("sum last two:", new_score, stack)

    else:
        stack.append(int(op))
        print("add score:", stack)

print("final stack:", stack)
print("total:", sum(stack))