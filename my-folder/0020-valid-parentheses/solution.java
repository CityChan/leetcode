class Solution {
    public boolean isValid(String s) {
        Deque<Character> stack = new ArrayDeque<>();
        for(char ch: s.toCharArray()){
            // if left, push
            if(ch=='('||ch =='{'||ch=='['){
                stack.addFirst(ch);
            }else{
                if(stack.isEmpty()){
                    return false;
                }
                char p = stack.pop();
                switch(ch){
                    case ')':
                        if(p=='('){
                            continue;
                        }
                        return false;
                    case ']':
                        if(p=='['){
                            continue;
                        }
                        return false;
                    case '}':
                        if(p=='{'){
                            continue;
                        }
                    default:
                        return false;
                }
            }
        }
        return stack.isEmpty();
    }
}
