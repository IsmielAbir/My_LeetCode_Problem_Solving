class Solution {
    public int missingNumber(int[] nums) {
        int n = nums.length;
        int a = n;
        for(int i=0;i<n;i++){
            a += i - nums[i];
        }
        return a;
    }
}