class Solution {
    public int[] sortArray(int[] a) {
        mergeSort(a, 0, a.length-1);
        return a;
    }

    public void merge(int[] arr, int l, int mid, int r){
        int n1 = mid - l + 1;
        int n2 = r - mid;

        int a[] = new int[n1];
        int b[] = new int[n2];

        for(int i=0;i<n1;i++){
            a[i] = arr[l+i];
        }
        for(int i=0;i<n2;i++){
            b[i] = arr[mid+1+i];
        }

        int i=0, j=0, k=l;
        while(i<n1 && j<n2){
            if(a[i]<=b[j])
                arr[k++] = a[i++];
            else
                arr[k++] = b[j++];
        }

        while(i<n1){
            arr[k++] = a[i++];
        }
        while(j<n2){
            arr[k++] = b[j++];
        }
    }

    public void mergeSort(int[] arr, int l, int r){
        if(l<r){
            int mid = (l + r)/2;
            mergeSort(arr, l, mid);
            mergeSort(arr, mid+1, r);
            merge(arr, l, mid, r);
        }
    }
}
