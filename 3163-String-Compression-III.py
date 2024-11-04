class Solution:
    def compressedString(self, word: str) -> str:
        if not word:
            return ""
        ct = 1
        st = ""
        cur_letter = word[0]
        for i in word[1:]:
            if i == cur_letter:
                if ct == 9:
                    st+="9"+cur_letter
                    ct = 1
                else:
                    ct+=1
            else:
                st+=str(ct)+cur_letter
                cur_letter = i
                ct = 1
        st+=str(ct)+cur_letter
        return st
            