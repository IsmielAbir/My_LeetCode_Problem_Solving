class Solution {
    public boolean isSameAfterReversals(int n) {
        int a=0, b=n,c=0;
        while(n!=0){
            int r = n%10;
            a = r + a*10;
            n/=10;
        }
        while(a!=0){
            int p = a%10;
            c = p + c*10;
            a/=10;
        }
        return c==b? true : false;
    }
}