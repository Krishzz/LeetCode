class Solution:
    def reverseWords(self, s: str) -> str:
        arr = [word for word in s.split() if word.isalpha() or word.isalnum() or word.isnumeric()]
        print(arr)
        return (\ \).join(arr[::-1]) if arr else s