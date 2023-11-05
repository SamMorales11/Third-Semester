def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less_than_pivot = [x for x in arr[1:] if x <= pivot]
        greater_than_pivot = [x for x in arr[1:] if x > pivot]
        return quick_sort(less_than_pivot) + [pivot] + quick_sort(greater_than_pivot)

# Contoh penggunaan
kode_barang = [564, 123, 789, 890, 234, 456, 678, 987, 654, 342, 567, 876, 109, 231, 567, 987, 321, 345, 678, 234, 543, 678, 890, 123, 567, 890, 234, 567, 789, 876, 109, 876, 231, 567, 987, 321, 345, 678, 890, 123, 567]
print("Kode barang awal:", kode_barang)

kode_barang_terurut = quick_sort(kode_barang)

print("Kode barang terurut:", kode_barang_terurut)