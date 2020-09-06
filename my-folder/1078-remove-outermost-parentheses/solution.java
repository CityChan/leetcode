class Solution {
    public String removeOuterParentheses(String S) {
        StringBuilder sb = new StringBuilder();
        int opened = 0;
        for (char c : S.toCharArray()) {
            // at least 
            if (c == '(') {
                if (opened > 0) sb.append(c);
                opened++;
            } else if (c == ')') {
                if (opened > 1) sb.append(c);
                opened--;
            }
        }
        return sb.toString();
    }
}
