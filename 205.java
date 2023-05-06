class Solution {
    public boolean isIsomorphic(String s, String t) {
        HashMap<Character, Integer> m1 = new HashMap<>();
        HashMap<Character, Integer> m2 = new HashMap<>();
        for(Integer i=0;i<s.length();i++){
            if(m1.put(s.charAt(i),i) != m2.put(t.charAt(i),i))
            return false;
        }
        return true;

    }
}