class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for  i in num:
            while stack and stack[-1]> i and k>0:
                stack.pop()
                k-=1
            stack.append(i)
        while stack and k!=0:
            stack.pop()
            k-=1
        str_stack = "".join(stack)
        str_stack = str_stack.lstrip("0")
        if str_stack =="":
            return "0"
        else:
            return str_stack