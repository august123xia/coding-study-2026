stack = []

stack.append("A")
print(stack)

stack.append("B")
print(stack)

stack.append("C")
print(stack)

top = stack[-1]
print("top:", top)

removed = stack.pop()
print("removed:", removed)
print(stack)

removed = stack.pop()
print("removed:", removed)
print(stack)