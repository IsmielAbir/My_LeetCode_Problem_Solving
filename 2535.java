class Solution {
    public int differenceOfSum(int[] nums) {
        int sum = 0, s=0;
        for(int i=0;i<nums.length;i++){
            sum+=nums[i];
        }
        for(int i=0;i<nums.length;i++){
            int num = nums[i];

            while(num!=0){
                int r = num%10;
                s += r;
                num/=10;
            }
        }
        return Math.abs(sum-s);
    }
}