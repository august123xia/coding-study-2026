def remove_duplicates(s):
    stack = []
    for char in s:
        if len(stack) != 0 and char == stack[-1] :
            stack.pop()
        
        else:
            stack.append(char)

    return "".join(stack)

print(remove_duplicates("abbaca"))   # ca
print(remove_duplicates("azxxzy"))   # ay
print(remove_duplicates("aabb"))     # 
print(remove_duplicates("abc"))      # abc

# Review:
# Stack follows Last In, First Out.
# In this problem, stack stores characters that have not been removed.
# If the current character is the same as the top of the stack, we pop it.
# Otherwise, we push the current character into the stack.
# "".join(stack) converts the list of characters back into a string.