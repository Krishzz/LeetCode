class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        hashmap = {}
        for word in words:
            st = ""
            for s in word:
                st+=s
                if st not in hashmap:
                    hashmap[st] = 0
                hashmap[st]+=1
        counts = [0]*len(words)
        for i in range(len(words)):
            st = ""
            for c in words[i]:
                st+=c
                if st in hashmap:
                    counts[i]+=hashmap[st]
        return counts
