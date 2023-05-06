class Solution {
    public int pivotIndex(int[] nums) {
        int rs=0, ls=0, n = nums.length;
        for(int i=0;i<n;i++){
            rs+=nums[i];
        }
        if(n == 0) 
        return 0;
        else{
            for(int i=0;i<n;i++){
                rs -= nums[i];
                if(rs == ls) 
                return i;
                else
                ls += nums[i];
            }
        }
        return -1;
    }
}