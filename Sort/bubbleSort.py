def bubbleSort(array):
    for i in range(len(array)):
        for j in range(len(array) - 1):
            if(array[j] > array[j+1]):
                array[j], array[j+1] = array[j+1], array[j]
    print(array)

if(__name__ == "__main__"):
    array = [5, 2, 1, 6, 2]
    bubbleSort(array)