class Solution:
    def isPalindrome(self, s: str) -> bool:
        ar = \\.join([st for st in s.lower() if st.isalnum()])
        return ar[::-1] == ar