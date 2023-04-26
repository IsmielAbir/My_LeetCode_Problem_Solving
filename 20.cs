public class Solution {
    public bool IsValid(string s) {
        Stack<char> st = new Stack<char>();
        foreach (char c in s) {
            if (c == '(' || c == '{' || c == '[') {
                st.Push(c);
            } else {
                if (c == ')' && st.Count > 0 && st.Peek() == '(') {
                    st.Pop();
                } else if (c == '}' && st.Count > 0 && st.Peek() == '{') {
                    st.Pop();
                } else if (c == ']' && st.Count > 0 && st.Peek() == '[') {
                    st.Pop();
                } else {
                    return false;
                }
            }
        }
        return st.Count == 0;
    }
}