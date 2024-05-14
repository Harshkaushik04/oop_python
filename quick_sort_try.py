def quick_sort(l):
    if len(l)>1:
        pivot=l[len(l)//2]
        lower_list=[x for x in l if x<pivot]
        middle_list=[x for x in l if x==pivot]
        upper_list=[x for x in l if x>pivot]
        l=quick_sort(lower_list)+middle_list+quick_sort(upper_list)
        return l
    else:
        return l
#example:
my_list = [342, 5, 23, 243, 63, 1, 643, 7, 5, 53, 4]
print(quick_sort(my_list))