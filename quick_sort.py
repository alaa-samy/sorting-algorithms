# Quick sort algorithm

def quickSort(array):
    if len(array) <= 1:
        return array
    else:
        pivot = array.pop()

    items_greater = []
    items_lower = []

    for i in array:
        if i > pivot:
            items_greater.append(i)

        else:
            items_lower.append(i)

    return quickSort(items_lower) + [pivot] + quickSort(items_greater)

if __name__ == '__main__':
    print('Write numbers separated by comma\'s')
    array =list(map(int, input().split(',')))
    print(quickSort(array))