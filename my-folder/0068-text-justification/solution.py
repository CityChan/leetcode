class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        res = []
        now_len = 0
        for word in words:
            if now_len == 0:
                now_len = len(word)
                temp_res = [word]
                temp_word_count = 1       
            elif now_len+len(word)+1<maxWidth:
                temp_res+=[word]
                temp_word_count+=1
                now_len += (len(word)+1)
            elif now_len+len(word)+1==maxWidth:
                temp_res+=[word]
                temp_str = temp_res[0]               
                for i in range(1, temp_word_count+1):
                    temp_str+=" "+temp_res[i]  
                res+=[temp_str]
                temp_word_count=0
                now_len = 0
                temp_res = []
            else:
                temp_str = temp_res[0]
                if temp_word_count==1:
                    temp_str += (maxWidth-now_len)*" "
                else:
                    space_len = (maxWidth-now_len)//(temp_word_count-1)
                    space_left = (maxWidth-now_len)%(temp_word_count-1)
                    for i in range(1, temp_word_count):
                        if space_left>0:
                            temp_str+=(2+space_len)*" "+temp_res[i]
                            space_left-=1
                        else:
                            temp_str+=(space_len+1)*" "+temp_res[i]
                res+=[temp_str]
                now_len = len(word)
                temp_res = [word]
                temp_word_count = 1
        if now_len>0:
            temp_str = " ".join(temp_res)
            temp_str+=(maxWidth-now_len)*" "
            # temp_str = temp_res[0]
            # if temp_word_count==1:
            #     temp_str += (maxWidth-now_len)*" "
            # else:
            #     space_len = (maxWidth-now_len)//(temp_word_count-1)
            #     space_left = (maxWidth-now_len)%(temp_word_count-1)
            #     for i in range(1, temp_word_count):
            #         if space_left>0:
            #             temp_str+=(2+space_len)*" "+temp_res[i]
            #             space_left-=1
            #         else:
            #             temp_str+=(space_len+1)*" "+temp_res[i]
            res+=[temp_str]
            
        return res
                            
                
                    
        
