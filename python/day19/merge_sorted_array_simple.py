def merge_sorted(nums1, nums2):
    i = 0
    j = 0
    result = []

    while i < len(nums1) and j < len(nums2):
        if nums1[i] < nums2[j]:
            result.append(nums1[i])
            i += 1
        else:
            result.append(nums2[j])
            j += 1

    while i < len(nums1):
        result.append(nums1[i])
        i += 1

    while j < len(nums2):
        result.append(nums2[j])
        j += 1

    return result


print(merge_sorted([1, 3], [2, 4, 6, 8]))      # [1, 2, 3, 4, 6, 8]
print(merge_sorted([1, 2, 3], [4, 5, 6]))      # [1, 2, 3, 4, 5, 6]
print(merge_sorted([], [1, 2, 3]))             # [1, 2, 3]
print(merge_sorted([1, 2, 3], []))             # [1, 2, 3]