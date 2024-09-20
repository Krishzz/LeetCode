class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        max_len = len(max(word1, word2, key=len))
        merged_string = ""
        l = 0
        while l<max_len:
            if l<len(word1):
                merged_string+=word1[l]
            if l<len(word2):
                merged_string+=word2[l]
            l+=1
        return merged_string

        