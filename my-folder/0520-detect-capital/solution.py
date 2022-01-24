class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if word.upper()==word or word.lower()==word or word.capitalize()==word:
            return True
        else:
            return False
