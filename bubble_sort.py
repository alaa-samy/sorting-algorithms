# Bubble sort algorithm

def swap(array , i , j):
    temp = array[i]
    array[i] = array[j]
    array[j] = temp

def bubbleSort(array):
    n = len(array) - 1
    for i in range(0,len(array)):
        for j in range(0, n):
            if array[j] > array[j+1]:
                swap(array , j+1 , j)

        n-=1

if __name__ == '__main__':
    print('Write numbers separated by comma\'s')
    array =list(map(int, input().split(',')))
    bubbleSort(array)
    print(array)