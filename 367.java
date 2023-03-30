import java.lang.Math;
class Solution {
    public boolean isPerfectSquare(int num) {
        if(((int)Math.sqrt(num)*(int)Math.sqrt(num))==num)
        return true;
        else 
        return false;
    }
}