class Solution {
    public int maximumCount(int[] nums) {
        int c=0, d=0;
        for(int i=0;i<nums.length;i++){
            if(nums[i]>0)
            c++;
            else if(nums[i]<0)
            d++;
        }
        return Math.max(c,d);
    }
}