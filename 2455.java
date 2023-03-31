class Solution {
    public int averageValue(int[] nums) {
        int c=0,a=0;
        for(int i=0;i<nums.length;i++){
            if(nums[i]%2==0 && nums[i]%3==0){
                c+=nums[i];
                a++;
            }
        }
        return a==0? 0 : c/a;
    }
}