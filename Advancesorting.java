public class Advancesorting {
    
}
public class QuickSort {
    public static void quickSort(int[] arr, int low, int high) {
        if (low < high) {
            int pivotIndex = partition(arr, low, high);
            quickSort(arr, low, pivotIndex - 1);
            quickSort(arr, pivotIndex + 1, high);
        }
    }

    public static int partition(int[] arr, int low, int high) {
        int pivot = arr[high];
        int i = low - 1;
        for (int j = low; j < high; j++) {
            if (arr[j] <= pivot) {
                i++;
                int temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
            }
        }
        int temp = arr[i + 1];
        arr[i + 1] = arr[high];
        arr[high] = temp;
        return i + 1;
    }

    public static void main(String[] args) {
        int[] kodeBarang = {564, 123, 789, 890, 234, 456, 678, 987, 654, 342, 567, 876, 109, 231, 567, 987, 321, 345, 678, 234, 543, 678, 890, 123, 567, 890, 234, 567, 789, 876, 109, 876, 231, 567, 987, 321, 345, 678, 890, 123, 567};
        System.out.print("Kode barang awal: ");
        for (int num : kodeBarang) {
            System.out.print(num + " ");
        }
        System.out.println();

        quickSort(kodeBarang, 0, kodeBarang.length - 1);

        System.out.print("Kode barang terurut: ");
        for (int num : kodeBarang) {
            System.out.print(num + " ");
        }
        System.out.println();
    }
}
