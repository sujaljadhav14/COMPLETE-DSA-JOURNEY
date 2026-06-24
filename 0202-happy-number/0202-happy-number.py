class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n!=1:
            if n in seen:
                return False
            seen.add(n)
            new_num=0
            while n>0:
                digit = n%10
                new_num += digit**2
                n=n//10
            n=new_num
        return True





        