def Sequential_Search(nlist, item):
    pos = 0
    found = False

    while pos < len(nlist) and not found:
        if nlist[pos] == item:
            found = True
        else:
            pos = pos + 1

    return found, pos


print(Sequential_Search([117,22,43,8,12,46,21,40], 21))
