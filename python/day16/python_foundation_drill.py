nums = [10, 20, 30, 40, 50]

for i, num in enumerate(nums):
    print(i, num)


print(len(nums))

print(nums[len(nums)-1])

Total = 0
for num in nums:
    Total = Total + num

print(Total)

Count = 0
for num in nums:
    if num > 25:
        Count += 1
    
print(Count)

nums = [1, 2, 3]

for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        print(nums[i], nums[j])