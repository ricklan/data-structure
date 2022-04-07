def mergeSort(array):
    n = len(array)

    if(n <= 1):
        return array
    
    i = n // 2
    l1 = array[:i]
    l2 = array[i:]
    
    l1 = mergeSort(l1)
    l2 = mergeSort(l2)

    return merge(l1, l2)

def merge(l1, l2):
    new_array = []
    while(len(l1) > 0 and len(l2) > 0):
        if(l1[0] < l2[0]):
            new_array.append(l1[0])
            l1.pop(0)
        elif(l1[0] > l2[0]):
            new_array.append(l2[0])
            l2.pop(0)
        else:
            new_array.append(l1[0])
            new_array.append(l2[0])
            l1.pop(0)
            l2.pop(0)
    
    if(len(l1) > 0):
        new_array += l1
    
    if(len(l2) > 0):
        new_array += l2
        
    return new_array

if(__name__ == "__main__"):
    array = [5, 2, 1, 6, 4]
    print(mergeSort(array))
    array2 = [5, 2, 1, 6, 4, 1, 1, 1, 1, 0]
    print(mergeSort(array2))
