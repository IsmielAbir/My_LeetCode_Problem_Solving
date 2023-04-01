class Solution {
    public int finalValueAfterOperations(String[] operations) {
        int a=0;
        for(String s:operations){
            if(s.charAt(1)=='+')
            a++;
            else
            a--;
        }
        return a;
    }
}