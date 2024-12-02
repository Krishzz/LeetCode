class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        arr = sentence.split(" ")
        for i in range(0,len(arr)):
            if arr[i][:len(searchWord)] == searchWord:
                return i+1
        return -1