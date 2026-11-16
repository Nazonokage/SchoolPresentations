public class test {

    void insertionSort(int[] arr) {
    for (int i = 1; i < arr.length; i++) {
        int current = arr[i], j = i - 1;
        // int 

        while (j >= 0 && arr[j] > current) {
            arr[j + 1] = arr[j];   // shift right
            j--;
        }
        arr[j + 1] = current;      // insert into gap
    }
}

}