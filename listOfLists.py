def group_and_sort(int_list):
    result = []
    int_set = set(int_list)

    for num in int_set:
        sublist = sorted([x for x in int_list if x == num])
        result.append(sublist)
    return result

print(group_and_sort([1,2,3,2,1,2,3,2,2,1,2,3,1,1,2,3,2,3,3,2,4,4,5,3,5,5,6]))


