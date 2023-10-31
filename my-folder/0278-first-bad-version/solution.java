/* The isBadVersion API is defined in the parent class VersionControl.
      boolean isBadVersion(int version); */

public class Solution extends VersionControl {
    public int firstBadVersion(int n) {
      int start = 1;
      int end = n;
      
      // exit case: start >= end
      while (start < end) {
        int mid = start + (end - start) / 2;
        if (isBadVersion(mid)) {
          // mid could be the right answer
          end = mid;
        } else {
          // mid could not be the right anwer
          start = mid + 1;
        }
      }
      
      return isBadVersion(end) ? end : start;
    }
}
