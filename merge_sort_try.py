def merge(left,right):
    i,j=0,0
    arr=[]
    while i<len(left) and j<len(right):
        if left[i]<=right[j]:
            arr.append(left[i])
            i+=1
        else:
            arr.append(right[j])
            j+=1
    arr+=left[i:]
    arr+=right[j:]
    return arr
def merge_sort(l):
    left,right=[],[]
    if len(l)<=1:
        return l
    mid=len(l)//2
    left=merge_sort(l[:mid])
    right=merge_sort(l[mid:])
    return merge(left,right)
# Example:
l = [3, 423, 342, 643, 465, 1, 45]
sorted_l = merge_sort(l)
print(sorted_l)

