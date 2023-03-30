class Solution {
    public boolean isPalindrome(int n) {
        int a=0;
        int p = n;
        if(n<0)
        return false;
        else{
        while(n!=0){
            int r = n%10;
            a  = r + a*10;
            n/=10;
        }
        return p==a;
        }
    }
}