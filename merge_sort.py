# Merge sort algorithm

def mergeSort(array):
    if len(array) > 1:
        left_array = array[:len(array)//2]
        right_array = array[len(array)//2:]

        mergeSort(left_array)
        mergeSort(right_array)

        i=0  # left array index
        j=0  # right array index
        k=0
        while i < len(left_array) and j < len(right_array):
            if left_array[i] < right_array[j]:
                array[k] = left_array[i]
                i+=1
                k+=1
            else:
                array[k] = right_array[j]
                j+=1
                k+=1

        while i < len(left_array):
            array[k] = left_array[i]
            i+=1
            k+=1

        while j < len(right_array):
            array[k] = right_array[j]
            j+=1
            k+=1

if __name__ == "__main__":
    print('Write numbers separated by comma\'s')
    array =list(map(int, input().split(',')))
    mergeSort(array)
    print(array)
