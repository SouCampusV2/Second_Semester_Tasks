def BubbleSort(array):
    for i in range(len(array)-1):
        for j in range(len(array)-i-1):
            # Если след число больше предыдущего меняем их местами, если нет проходим дальше
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]

    print(array)

arr = [1,2,3,4,1,2,10,15,2,3,4]
BubbleSort(arr)