import java.util.Stack;

class Solution {
    public boolean isValid(String s) {
        Stack<Character> st = new Stack<>();
        for(char c: s.toCharArray()){
            if(c=='(' || c=='{' || c=='[')
            st.push(c);
            else{
                if(c==')' && !st.empty() && st.peek()=='(')
                st.pop();
                else if(c=='}' && !st.empty() && st.peek()=='{')
                st.pop();
                else if(c==']' && !st.empty() && st.peek()=='[')
                st.pop();
                else
                return false;
            }
        }

        return st.empty();       

    }
}