class Solution {
    public List<Boolean> kidsWithCandies(int[] candies, int extraCandies) {
        int c=0;
        List<Boolean> result = new ArrayList<>();
        for(int candy : candies){
            c = Math.max(candy, c);
        }
        for(int candy : candies){
            result.add(candy+extraCandies>=c);
        }
        return result;

    }
}