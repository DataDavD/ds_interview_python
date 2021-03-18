from typing import List


# brute force driving through the list fully once and list n-1
# so O(n^2) time complexity
def find_product(lst: List[int]) -> List[int]:
    result = list()
    for x in range(len(lst)):
        product = 1
        for i in lst:
            if i != lst[x]:
                product *= i
        result.append(product)
    return result


# O(n^2) because list iterated over n(n-1)/2
def find_product_sol1(lst: List[int]) -> List[int]:
    result = []
    left = 1  # To store product of all previous values from currentIndex
    for i in range(len(lst)):
        currentproduct = 1  # To store current product for index i
        # compute product of values to the right of i index of list
        for ele in lst[i + 1 :]:
            currentproduct = currentproduct * ele
        # currentproduct * product of all values to the left of i index
        result.append(currentproduct * left)
        # Updating `left`
        left = left * lst[i]

    return result


# O(n) since only traverse the list twice
def find_product_sol2(lst: List[int]) -> List[int]:
    # get product start from left
    left = 1
    product = []
    for ele in lst:
        product.append(left)
        left *= ele
    # get product starting from right
    right = 1
    for i in range(len(lst) - 1, -1, -1):
        product[i] *= right
        right *= lst[i]

    return product
