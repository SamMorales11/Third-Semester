import java.util.Arrays;
import java.util.Random;

public class MergeSortExample {
    public static void main(String[] args) {
        Random rand = new Random();
        int[] numbers = new int[10];

        // Mengisi array dengan bilangan acak antara 0 hingga 99
        for (int i = 0; i < numbers.length; i++) {
            numbers[i] = rand.nextInt(100);
        }

        System.out.println("Before sorting:");
        printArray(numbers);

        mergeSort(numbers);

        System.out.println("\nAfter sorting:");
        printArray(numbers);
    }

    private static void mergeSort(int[] inputArray) {
        int inputLength = inputArray.length;

        if (inputLength <= 1) {
            return;
        }

        int midIndex = inputLength / 2;
        int[] leftHalf = Arrays.copyOfRange(inputArray, 0, midIndex);
        int[] rightHalf = Arrays.copyOfRange(inputArray, midIndex, inputLength);

        mergeSort(leftHalf);
        mergeSort(rightHalf);

        merge(inputArray, leftHalf, rightHalf);
    }

    private static void merge(int[] inputArray, int[] leftHalf, int[] rightHalf) {
        int leftSize = leftHalf.length;
        int rightSize = rightHalf.length;

        int i = 0, j = 0, k = 0;

        while (i < leftSize && j < rightSize) {
            if (leftHalf[i] <= rightHalf[j]) {
                inputArray[k++] = leftHalf[i++];
            } else {
                inputArray[k++] = rightHalf[j++];
            }
        }

        while (i < leftSize) {
            inputArray[k++] = leftHalf[i++];
        }

        while (j < rightSize) {
            inputArray[k++] = rightHalf[j++];
        }
    }

    private static void printArray(int[] numbers) {
        for (int number : numbers) {
            System.out.print(number + " ");
        }
        System.out.println();
    }
}