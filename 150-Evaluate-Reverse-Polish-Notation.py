class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        arr = []
        operation = set(['+', '-', '*', '/'])
        for i in tokens:
            if i in operation:
                a,b = arr.pop(), arr.pop()
                if i == \+\:
                    arr.append(a+b)
                elif i == \-\:
                    arr.append(b-a)
                elif i == \*\:
                    arr.append(a*b)
                elif i == \/\:
                    arr.append(int(b/a))
            else:
                arr.append(int(i))
        return arr[0]
        