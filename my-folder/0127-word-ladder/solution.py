class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        # if beginWord==endWord:
        #     return 1
        
        word_dict = collections.defaultdict(set)
        for word in wordList:
            for i in range(len(word)):
                # if i<len(word):
                    word_dict[word[:i]+"_"+word[i+1:]].add(word)
                # else:
                #     word_dict[word[:i]+"_"].add(word)
        
        # step = 0
        
        # def bfs(now_word):
        #     for i in range(len(word)):
        #         if i<len(word)-1:
        #             temp_word = word[:i]+"_"+word[i+1:]
        #         else:
        #             temp_word = word[:i]+"_"
        #     for
        step = 0
        q = [beginWord]
        visited = set([beginWord])
        while q:
            sz = len(q)
            step+=1
            for _ in range(sz):
                word = q.pop(0)
                if word==endWord:
                    return step
                for i in range(len(word)):
                    # if i<len(word)-1:
                    temp_word = word[:i]+"_"+word[i+1:]
                    # else:
                    #     temp_word = word[:i]+"_"
                    for nxt in word_dict[temp_word]:
                        # if nxt==endWord:
                        #     return step
                        # else:
                            if nxt not in visited:
                                visited.add(nxt)
                                q.append(nxt)
        return 0

                
        
