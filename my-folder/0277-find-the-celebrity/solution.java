/* The knows API is defined in the parent class Relation.
      boolean knows(int a, int b); */

public class Solution extends Relation {
    public int findCelebrity(int n) {
        int cadidate = 0;
        for(int i=1;i<n;i++){
            if(knows(cadidate, i)){
                cadidate = i;
            }
        }
        for(int i=0;i<n;i++){
            if(i>cadidate&&!knows(i, cadidate)){
                return -1;
            }
            if(i<cadidate&&(knows(cadidate, i) || !knows(i, cadidate))){
                return -1;
            }
        }
        return cadidate;
    }
}
