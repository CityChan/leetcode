class Solution {
    public int calculate(String s) {
        // Deque<Integer> operands = new LinkedList<>();
        char sign = '+';
        int num = 0;
        int prev = 0;
        int res = 0;
        for(int i=0;i<s.length();++i){
            char ch = s.charAt(i);
            if(Character.isDigit(ch)){
                num = num * 10 + (ch-'0');
            }
            if(i==s.length()-1|| !Character.isDigit(ch)&&ch!=' '){ // operators
                if(sign=='+'){
                    res += prev;
                    prev = num;
                }else if(sign=='-'){
                    res += prev;
                    prev = -num;
                }else if(sign=='*'){
                    prev *= num;
                }else{
                    prev /= num;
                }
                num = 0;
                sign = ch;
            }
        }
        return res+prev;
    }

}
