def binary_search(nlist, item):
    first = 0
    last = len(nlist) - 1
    found = False
    while (first <= last and not found):
        mid = (first + last) // 2
        if nlist[mid] == item:
            found = True
        else:
            if item < nlist[mid]:
                last = mid - 1
            else:
                first = mid + 1
    return found


print(binary_search([1, 2, 3, 5, 8], 6))
print(binary_search([1, 2, 3, 5, 8], 5))
