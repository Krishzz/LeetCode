class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hashmap = {
            ')':'(',
            '}':'{',
            ']':'['
        }
        for i in s:
            if i in hashmap:
                if (len(stack)==0) or (stack[-1] != hashmap[i]):
                    return False
                stack.pop()
            else:
                stack.append(i)
        return len(stack)==0