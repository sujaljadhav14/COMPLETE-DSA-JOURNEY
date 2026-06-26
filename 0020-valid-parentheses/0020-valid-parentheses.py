class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        pairs = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        for ch in s:
            if ch in "([{":
                stack.append(ch)
            else:
                if stack ==[]:
                    return False
                if stack[-1]!= pairs[ch]:
                    return False
                """
                if ch == ")" and top != "(":
                    return False

                if ch == "]" and top != "[":
                    return False

                if ch == "}" and top != "{":
                    return False
                """
                stack.pop()
        return len(stack) == 0