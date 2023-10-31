class MyQueue {
    Stack<Integer> stack1 = new Stack<>();
    Stack<Integer> stack2 = new Stack<>();

    public MyQueue() {

    }
    
    public void push(int x) {
      stack1.add(x);
    }
    
    public int pop() {
      if (stack2.isEmpty()) {
        while (!stack1.isEmpty()) {
          stack2.push(stack1.pop());
        }
      }
      if (!stack2.isEmpty()) {
        return stack2.pop();
      } else {
        throw new IllegalStateException("Queue is empty");
      }
    }
    
    public int peek() {
      if (stack2.isEmpty()) {
        while (!stack1.isEmpty()) {
          stack2.push(stack1.pop());
        }
      }
       if (!stack2.isEmpty()) {
        return stack2.peek();
      } else {
        throw new IllegalStateException("Queue is empty");
      }
    }
    
    public boolean empty() {
      return stack1.isEmpty() && stack2.isEmpty();
    }
}

/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue obj = new MyQueue();
 * obj.push(x);
 * int param_2 = obj.pop();
 * int param_3 = obj.peek();
 * boolean param_4 = obj.empty();
 */
