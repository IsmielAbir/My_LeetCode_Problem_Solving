class Solution {
    public boolean checkPerfectNumber(int n) {
        if(n==1)
        return false;
         int sum = 1;
    for (int i = 2; i <= Math.sqrt(n); i++) {
        if (n % i == 0) {
            sum += i;
            if (i != n/i) {
                sum += n/i;
            }
        }
    }
    return sum == n;
    }
}