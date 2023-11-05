def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Contoh penggunaan
nilai_awal = [64, 34, 25, 12, 22, 11, 90, 56, 78, 1]
print("Nilai awal:", nilai_awal)

bubble_sort(nilai_awal)

print("Nilai terurut:", nilai_awal)