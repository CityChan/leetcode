class Solution {
    // letter logs -> lexicographically, use id in case of ties
    // digit logs -> original 
    public String[] reorderLogFiles(String[] logs) {
        Arrays.sort(logs,(a,b)->{
            int iA = a.indexOf(" ");
            int iB = b.indexOf(" ");
            
            char chA = a.charAt(iA+1);
            char chB = b.charAt(iB+1);
            // both are digits -> original
            // both are letters -> compare
            // A is digit, B is letter -> B, A
            // A is letter, B is digit -> A, B 
            if(chB>='0'&&chB<='9'){
                return chA>='0'&&chA<='9'? 0:-1;
            }
            if(chA>='0'&&chA<='9'){
                return 1;
            }
            
            int diff = a.substring(iA+1).compareTo(b.substring(iB+1));
            if(diff==0){
                return a.substring(0,iA).compareTo(b.substring(0, iB));
            }
            return diff;
        });
        
        return logs;
    }
}
