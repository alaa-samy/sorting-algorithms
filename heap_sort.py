# Heap sort algorithm

def swap(array , i , j):
    temp = array[i]
    array[i] = array[j]
    array[j] = temp

def heapSort(array):
    heapify(array, len(array))
    end = len(array)-1
    while end > 0:
        swap(array , 0 , end)
        end -= 1
        shiftDown(array, 0, end)

def heapify(array, count):
    start = int((count-2)/2)
    while start >= 0:
        shiftDown(array, start, count-1)
        start -= 1

def shiftDown(array, start, end):
    root = start
    while (root*2+1) <= end:
        child = root * 2 + 1
        swap = root
        if array[swap] < array[child]:
            swap = child
        if (child + 1) <= end and array[swap] < array[child+1]:
            swap = child+1
        if swap != root:
            array[root], array[swap] = array[swap], array[root]
            root = swap
        else:
            return

if __name__ == "__main__":
    print('Write numbers separated by comma\'s')
    array =list(map(int, input().split(',')))
    heapSort(array)
    print(array)