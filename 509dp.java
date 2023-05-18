class Solution {
    int[] ar = new int[31];

    public int fib(int n) {
        if(n==0)
        return 0;
        if (n == 1 || n==2)
            return 1;
        ar[n] = fib(n - 1) + fib(n - 2);
        return ar[n];
    }
}
