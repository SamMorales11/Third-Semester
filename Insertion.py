def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j>= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
            arr [j+1] = key


#Example
arr = [111,654,1,2,45,67,98,99,324]
insertion_sort (arr)
print ("Sorted array", arr)