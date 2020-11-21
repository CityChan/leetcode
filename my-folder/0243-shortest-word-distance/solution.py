class Solution:
    def shortestDistance(self, words: List[str], word1: str, word2: str) -> int:
        size = len(words)
        pos1, pos2 = size, size
        result = size
        for i, word in enumerate(words):
            if word == word1:
                pos1 = i
                result = min(result, abs(pos1 - pos2))
            elif word == word2:
                pos2 = i
                result = min(result, abs(pos1 - pos2))
        return result
