# Insertion sort algorithm

def swap(array , i , j):
    temp = array[i]
    array[i] = array[j]
    array[j] = temp

def insertionSort(array):
    for i in range(0 , len(array)):
        j = i
        while j>0 and array[j-1]  >array[j]:
            swap(array, j-1 , j)
            j -=1

if __name__ == '__main__':
    print('Write numbers separated by comma\'s')
    array = list(map(int, input().split(',')))
    insertionSort(array)
    print(array)