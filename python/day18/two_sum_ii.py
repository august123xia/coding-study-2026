numbers = [2, 7, 11, 15]
target = 9

left = 0
right = len(numbers) - 1

while left < right:
    total = numbers[left] + numbers[right]
    print(left, right, numbers[left], numbers[right], total)

    if total == target:
        print("found")
        break
    elif total < target:
        left += 1
    else:
        right -= 1

def two_sum_ii(numbers, target):
    left = 0 
    right = len(numbers) -1 

    while left < right:
        total = numbers[left] + numbers[right]

        if total  == target:
            return [left+1, right+1]
        
        elif total < target:
            left += 1
        else: 
            right -=1

print(two_sum_ii([2, 7, 11, 15], 9))      # [1, 2]
print(two_sum_ii([2, 3, 4], 6))           # [1, 3]
print(two_sum_ii([-1, 0], -1))            # [1, 2]
