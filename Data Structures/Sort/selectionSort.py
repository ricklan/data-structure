def selectionSort(array):
    
    for i in range(len(array)):
        minElement = array[i]
        counter = i
        for j in range(i + 1, len(array)):
            if array[j] < minElement:
                minElement = array[j]
                counter = j
        array.pop(counter)
        array.insert(i, minElement)
    print(array)

if(__name__ == "__main__"):
    array = [5, 2, 1, 6, 4]
    selectionSort(array)