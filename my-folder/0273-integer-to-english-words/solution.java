class Solution {
    private final String[] LESS_THAN_TWENTY= {
        "", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine",
        "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"};
    private final String[] TENS = {
        "", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"};
    private final int TEN = 10;
    private final int HUNDRED = 100;
    private final int THOUSAND = 1000;
    private final int MILLION = 1000000;
    private final int BILLION = 1000000000;
    
    public String numberToWords(int num) {
        if (num == 0) return "Zero";
        return helper(num);
    }
    
    private String helper(int num) {
        String res = "";
        if (num < 20) {
            res = LESS_THAN_TWENTY[num];
        } else if (num < HUNDRED) {
            res = TENS[num / 10] + " " + helper(num % 10);
        } else if (num < THOUSAND) {
            res = helper(num / HUNDRED) + " Hundred " + helper(num % HUNDRED);
        } else if (num < MILLION) {
            res = helper(num / THOUSAND) + " Thousand " + helper(num % THOUSAND);
        } else if (num < BILLION) {
            res = helper(num / MILLION) + " Million " + helper(num % MILLION);
        } else {
            res = helper(num / BILLION) + " Billion " + helper(num % BILLION);
        }
        return res.trim();
    }
}
