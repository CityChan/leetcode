class Solution {
    interface Operation {
        int operation(int x, int y);
    }
    public int evalRPN(String[] tokens) {
        Map<String, Operation> operators = new HashMap<>();
        operators.put("+", (a, b) -> a + b);
        operators.put("-", (a, b) -> a - b);
        operators.put("*", (a, b) -> a * b);
        operators.put("/", (a, b) -> a / b);
        
        Deque<Integer> stack = new LinkedList<>();
        for(String str: tokens){
            if(operators.containsKey(str)){
                int op2 = stack.pop();
                int op1 = stack.pop();
                int result = operators.get(str).operation(op1, op2);
                stack.push(result);
            } else {
                stack.push(Integer.parseInt(str));
            }
        }
        
        return stack.pop();
    }
}
