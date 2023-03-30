class Solution {
    public int reverse(int n) {
        long a=0;
       
        while(n!=0){
            int r = n%10;
            a = r+ a*10;
            n/=10;
        }
            return a < Integer.MIN_VALUE || a > Integer.MAX_VALUE ? 0 : (int)a;
    }
}