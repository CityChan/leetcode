class Solution {
    String[] lessThan20 = {"", "One", "Two", "Three","Four","Five", "Six","Seven","Eight","Nine",
                    "Ten", "Eleven", "Twelve", "Thirteen","Fourteen","Fifteen", "Sixteen","Seventeen","Eighteen","Nineteen"};
    String[] tens = {"", "", "Twenty", "Thirty","Forty","Fifty", "Sixty","Seventy","Eighty","Ninety"};
    String[] levels = {"", " Thousand", " Million"," Billion"};
    
    public String numberToWords(int num) {
        if(num==0){
            return "Zero";
        }
        int level = 0;
        String res = "";
        while(num!=0){
            int three = num % 1000;
            if(three!=0){
                StringBuilder sb = new StringBuilder();
                sb.append(threeDigits(three)).append(levels[level]);
                if(res.length()>0){
                    sb.append(" ").append(res);
                }
                res = sb.toString();
            }
            num = num/1000;
            level++;
        }
        return res;
    }
    public String threeDigits(int num) {
        if(num<20){
            return lessThan20[num];
        }
        if(num<100){
            int last = num%10;
            if(last==0){
                return tens[num/10];
            }
            return  tens[num/10] + " " + lessThan20[last];
        }
        int hundred = num /100;
        int rest = num % 100;
        if(rest!=0){
            return lessThan20[hundred] + " Hundred "+ threeDigits(rest);
        }
        return lessThan20[hundred] + " Hundred";
    }
}
