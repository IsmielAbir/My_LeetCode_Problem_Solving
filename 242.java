class Solution {
    public boolean isAnagram(String s, String t) {
        char[] c  = s.toCharArray();
        char[] ch = t.toCharArray();
        Arrays.sort(c);
        Arrays.sort(ch);
        return Arrays.equals(c, ch);
    }
}