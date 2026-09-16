def cal_points(ops):
    stack = []
    for op in ops:

        if op == "C":
            stack.pop()
        
        elif op == "D":
            double = stack[-1] * 2
            stack.append(double)
        
        elif op == "+":
            two = stack[-1] + stack[-2]
            stack.append(two)

        else:
            stack.append(int(op))
    
    return sum(stack)

print(cal_points(["5", "2", "C", "D", "+"]))          # 30
print(cal_points(["5", "-2", "4", "C", "D", "9", "+", "+"]))  # 27
print(cal_points(["1", "C"]))                         # 0

# Review:
# Stack follows Last In, First Out.
# In this problem, stack stores valid scores.
# "C" removes the previous score with pop().
# "D" adds double the previous score.
# "+" adds the sum of the previous two scores.
# Number strings need to be converted with int(op).
# sum(stack) returns the final total score.