class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack = []
        for ch in s:
            if ch == "#":
                if stack:
                    stack.pop()
            else:
                stack.append(ch)
        s_stack = "".join(stack)
        stack = []
        for ch in t:
            if ch == "#":
                if stack:
                    stack.pop()
            else:
                stack.append(ch)
        t_stack = "".join(stack)
        return s_stack == t_stack