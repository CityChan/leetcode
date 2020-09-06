class Solution {
    public int minAddToMakeValid(String S) {
        int left = 0;
        int right = 0;
        for (char c : S.toCharArray()) {
            if (c == '(') {
                right++;
            } else {
                if (right > 0) {
                    right--;
                } else {
                    left++;
                }
            }
        }
        return left + right;
    }
}
