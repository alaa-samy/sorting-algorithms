# Selection sort algorithm

def swap(array , i , j):
    temp = array[i]
    array[i] = array[j]
    array[j] = temp

def selectionSort(array):
    for i in range(0 , len(array)):
        minValue = i
        for j in range(i+1, len(array)):
            if array[j] < array[minValue]:
                minValue = j

        swap(array , i , minValue)

if __name__ == '__main__':
    print('Write numbers separated by comma\'s')
    array = list(map(int, input().split(',')))
    selectionSort(array)
    print(array)
