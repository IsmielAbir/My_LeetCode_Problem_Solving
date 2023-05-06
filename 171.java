class Solution {
    public int titleToNumber(String columnTitle) {
        int n=0;
        for(int i=0;i<columnTitle.length();i++){
            int c = columnTitle.charAt(i) - 'A' +1;
            n = n * 26 + c;
        }
        return n;

    }
}