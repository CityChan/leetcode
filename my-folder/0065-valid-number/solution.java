class Solution {
    public boolean isNumber(String s) {
        char[] str = s.trim().toCharArray();
        // int start = 0;
        // if(str[0]=='+'||str[0]=='-'){
        //     ++start;
        // }
        
        boolean hasDigitBeforeExponent = false;
        boolean exponent = false;
        boolean hasDigitAfterExponent = false;
        boolean hasDecimal = false;
        for(int i=0;i<str.length;++i){
            if(Character.isDigit(str[i])){
                if(exponent){
                    hasDigitAfterExponent = true;
                }else{
                    hasDigitBeforeExponent = true;
                }
            }else if(str[i]=='.'){
                if(exponent||hasDecimal){
                    return false;
                }
                hasDecimal = true;
            }else if(str[i]=='e'){
                if(exponent||!hasDigitBeforeExponent){
                    return false;
                }
                exponent = true;
            }else if(str[i]=='+'||str[i]=='-'){
                if(i!=0&&str[i-1]!='e'){
                    return false;
                }
            }else{
                return false;
            }
        }
        return exponent? hasDigitAfterExponent: hasDigitBeforeExponent;
    }
}
