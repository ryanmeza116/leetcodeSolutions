def group_and_sort(int_list):
    result = []
    int_set = set(int_list)

    for num in int_set:
        sublist = sorted([x for x in int_list if x == num])
        result.append(sublist)
    return result

print(group_and_sort([1,2,3,2,1,2,3,2,2,1,2,3,1,1,2,3,2,3,3,2,4,4,5,3,5,5,6]))




# def multiplyBy2(list):
#     new_list = []
#     for i in list:
#         new_list.append(i*2)
#     return new_list
# print(multiplyBy2([2,4,6]))

# def multiplyBytwo(list):
#     for i, element in enumerate(list):
#         list[i] = element * 2 
#     return list

# print(multiplyBytwo([2,3,4]))


