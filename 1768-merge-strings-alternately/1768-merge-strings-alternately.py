class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        new_word = ""

        lenWord_1 = len(word1)
        lenWord_2 = len(word2)

        if lenWord_1 < lenWord_2:
            for i in range(len(word1)):
                new_word += word1[i] + word2[i]
            new_word += word2[len(word1): ]     
            return new_word

        else:
            for i in range(len(word2)):
                new_word += word1[i] + word2[i]
            new_word += word1[len(word2): ] 
            return new_word


