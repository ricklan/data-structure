def quickSort(array):

    # Base Case
    if(len(array) <= 1):
        return array
    
    # Pivoting
    pivot = array[-1]
    less_than = []
    greater_than = []
    for i in range(len(array) - 1):
        item = array[i]
        if(item <= pivot):
            less_than.append(item)
        else:
            greater_than.append(item)

    # Combining it together
    return quickSort(less_than) + [pivot] + quickSort(greater_than)

if(__name__ == "__main__"):
    array = [5, 2, 1, 6, 4]
    print(quickSort(array))