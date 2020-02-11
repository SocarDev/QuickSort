def Quick_Sort(list):
    tam = len(list)
    if tam <= 1:
        return list
    else:
        pivot = list.pop()

    items_mayors = []
    items_manors = []

    for item in list:
        if item > pivot:
            items_mayors.append(item)

        else:
            items_manors.append(item)
    return Quick_Sort(items_manors) + [pivot] + Quick_Sort(items_mayors)


print(Quick_Sort([12, 122, 5, 0, -1, 19, 1000, 2, 6, 82, 123, 366, 23]))
