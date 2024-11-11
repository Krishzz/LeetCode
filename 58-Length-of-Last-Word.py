class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        arr = [word for word in s.split(' ') if word.isalpha()]
        return len(arr[-1]) if arr else 0
        