def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
             arr[j], arr[j+1] = arr[j+1], arr[j]


# Contoh Usage
arr = [111,45,68,768,999,10134,125,6756,99999]
bubble_sort(arr)
print("Sorted array:",arr)             