
def interpolationSearch(nlist, item):
    first = 0
    last = len(nlist) - 1
    found = False
    while first <= last and x >= nlist[first] and x <= nlist[last]:
        if first== last:
            if nlist[first] == x:
                return first;
            return -1;

        pos = first + int(((float(last - first) /
                         (nlist[last] - nlist[first])) * (x - nlist[first])))
        if nlist[pos] == x:
            return pos
        if nlist[pos] < x:
            first = pos + 1;
        else:
            last = pos - 1;

    return -1

print(interpolationSearch([1, 2, 3, 5, 8], 6))
print(interpolationSearch([1, 2, 3, 5, 8], 5))
