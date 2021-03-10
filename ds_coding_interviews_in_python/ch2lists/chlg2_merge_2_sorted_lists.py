from typing import List


# Merge list1 and list2 and return resulted list
def merge_lists_new(lst1, lst2):
    # O(n+m) where n and m are lengths of lst1 and lst2; have to iterate over both lists
    index_arr1 = 0
    index_arr2 = 0
    index_result = 0
    result = []

    for i in range(len(lst1) + len(lst2)):
        result.append(i)
    # Traverse Both lists and insert smaller value from arr1 or arr2
    # into result list and then increment that lists index.
    # If a list is completely traversed, while other one is left then just
    # copy all the remaining elements into result list
    while (index_arr1 < len(lst1)) and (index_arr2 < len(lst2)):
        if lst1[index_arr1] < lst2[index_arr2]:
            result[index_result] = lst1[index_arr1]
            index_result += 1
            index_arr1 += 1
        else:
            result[index_result] = lst2[index_arr2]
            index_result += 1
            index_arr2 += 1
    while index_arr1 < len(lst1):
        result[index_result] = lst1[index_arr1]
        index_result += 1
        index_arr1 += 1
    while index_arr2 < len(lst2):
        result[index_result] = lst2[index_arr2]
        index_result += 1
        index_arr2 += 1
    return result


# Merge list1 and list2 and return resulted list
def merge_lists_inplace(lst1, lst2):
    # O(m(n+m)) where n and m are the lengths of the lists

    # create 2 new vars to track current index
    ind1 = 0
    ind2 = 0

    # while both indices are less than their respective list lengths
    while ind1 < len(lst1) and ind2 < len(lst2):
        # if the curr element of lst1 > curr element of lst2
        if lst1[ind1] > lst2[ind2]:
            # insert list2's current index value to list1
            lst1.insert(ind1, lst2[ind2])
            ind1 += 1
            ind2 += 1
        else:
            ind1 += 1

    if ind2 < len(lst2):  # append whatever left of list2 to list1
        lst1.extend(lst2[ind2:])
    return lst1
