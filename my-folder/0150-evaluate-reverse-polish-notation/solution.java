class Solution {
    public interface Token {
    void process(Deque<Integer> stack);

  }

  public class Operand implements Token {
    private final int val;

    public Operand(int val) {
      this.val = val;
    }

    @Override
    public void process(Deque<Integer> stack) {
      stack.push(val);
    }
  }

  public abstract class BinaryOperator implements Token {
    private static final int numOfOperand = 2;

    @Override
    public void process(Deque<Integer> stack) {
      if (stack == null) {
        throw new IllegalArgumentException("Stack is empty");
      }
      if (stack.size() < numOfOperand) {
        throw new IllegalArgumentException("There is not enough elements to calculate");
      }

      int num2 = stack.pop();
      int num1 = stack.pop();
      stack.push(cal(num1, num2));
    }

    protected abstract int cal(int a, int b);
  }

  public abstract class UnaryOperator implements Token {
    private static final int numOfOperand = 1;

    @Override
    public void process(Deque<Integer> stack) {
      if (stack == null) {
        throw new IllegalArgumentException("Stack is empty");
      }
      if (stack.size() < numOfOperand) {
        throw new IllegalArgumentException("There is not enough elements to calculate");
      }

      stack.push(cal(stack.pop()));
    }

    protected abstract int cal(int a);
  }

  public class SquareRoot extends UnaryOperator {
    @Override
    protected int cal(int a) {
      return (int) Math.sqrt(a);
    }
  }


  public class Divide extends BinaryOperator {
    @Override
    protected int cal(int a, int b) {
      return a / b;
    }
  }

  public class Add extends BinaryOperator {
    @Override
    protected int cal(int a, int b) {
      return a + b;
    }
  }

  public class Subtract extends BinaryOperator {
    @Override
    protected int cal(int a, int b) {
      return a - b;
    }
  }

  public class Multiply extends BinaryOperator {
    @Override
    protected int cal(int a, int b) {
      return a * b;
    }
  }

  private Token parseToken(String token) {
    switch (token) {
      case "+":
        return new Add();
      case "-":
        return new Subtract();
      case "*":
        return new Multiply();
      case "/":
        return new Divide();
      case "sqrt":
        return new SquareRoot();
      default:
        try {
          return new Operand(Integer.parseInt(token));
        } catch (NumberFormatException e) {
          throw new IllegalArgumentException("Invalid Reverse Polish Token Found: " + token, e);
        }
    }
  }

  public int evalRPN(String[] tokens) {

    Deque<Integer> stack = new ArrayDeque<>();
    for (String str : tokens) {
      parseToken(str).process(stack);
    }

    return stack.pop();
  }
}
