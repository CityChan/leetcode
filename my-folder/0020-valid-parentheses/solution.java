class Solution {
  
    private Map<Character, Character> mappings; 
  
    public Solution() {
      this.mappings = new HashMap<>();
      this.mappings.put(')', '(');
      this.mappings.put('}', '{');
      this.mappings.put(']', '[');
    }
  
    public boolean isValid(String s) {
      if (s == null || s.length() == 0) {
        return true;
      }
      
      Stack<Character> stack = new Stack<>();
      for (char c : s.toCharArray()) {
        if (this.mappings.containsKey(c)) {
          // look up top of stack 
          if (stack.isEmpty()) {
            return false;
          }
          // if not matching 
          if (stack.peek() != this.mappings.get(c)) {
            return false;
          }
          stack.pop();
        } else {
          stack.push(c);
        }
      }
      return stack.isEmpty();
    }
}
