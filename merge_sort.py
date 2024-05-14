def merge_sort(l):
    # Creating empty lists for the left and right halves of the input list.
    left = []
    right = []
    #for completion of recursion
    if len(l) <= 1:
        return l
    # Find the middle index of the list.
    mid = len(l) // 2
    # Recursively apply merge_sort to the left and right halves of the list.
    left = merge_sort(l[:mid])
    right = merge_sort(l[mid:])
    # Merge the sorted left and right halves and return the result.
    return merge(left, right)

#function for merging two lists
def merge(left, right):
    i, j = 0, 0
    merged = []  # Create an empty list to store the merged result.
    # Comparing elements of left and right list
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    # Append any remaining elements from left and right to merged
    merged += left[i:]
    merged += right[j:]
    return merged

# Example:
l = [3, 423, 342, 643, 465, 1, 45]
sorted_l = merge_sort(l)
print(sorted_l)