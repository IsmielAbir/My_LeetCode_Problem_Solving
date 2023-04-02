class Solution {
    public int subtractProductAndSum(int n) {
        int a=0,b=1;
        while(n!=0){
            int r = n%10;
            a+= r;
            b*=r;
            n/=10;
        }
        return b-a;
    }
}