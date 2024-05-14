def quick_sort(l):
    #base case for recursion:
    if len(l) > 1:
        #chosing a pivot(could have chosen any element)
        pivot = l[len(l) // 2]
        # Creating three lists to hold elements smaller, equal, and larger than the pivot.
        lower_list = [x for x in l if pivot > x]
        middle_list = [x for x in l if pivot == x]
        upper_list = [x for x in l if pivot < x]
        # Recursively sort the lower and upper lists,and joining all
        l = quick_sort(lower_list) + middle_list + quick_sort(upper_list)
        return l #returning sorted list
    else:
        return l #list having 1 element is already sorted
#example:
my_list = [342, 5, 23, 243, 63, 1, 643, 7, 5, 53, 4]
print(quick_sort(my_list))