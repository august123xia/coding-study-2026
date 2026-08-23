def contains_duplicate(nums):
    seen = set()

    for num in nums:
        print("num:", num, "seen:", seen)

        if num in seen:
            print("Found duplicate:", num)
            return True
        
        seen.add(num)

    return False


nums = [5, 8, 9, 5, 10]
answer = contains_duplicate(nums)

print("answer:", answer)