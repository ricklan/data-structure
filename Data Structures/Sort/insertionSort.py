def insertionSort(array):
    for i in range(1, len(array)):
        counter = i
        j = i - 1
        tmp = array[i]
        while(j >= 0 and array[j] > tmp):
            counter = j
            j -= 1
        array.pop(i)
        array.insert(counter, tmp)
    print(array)

if(__name__ == "__main__"):
    array = [3, 1, 5, 3, 7, 2, -9]
    insertionSort(array)