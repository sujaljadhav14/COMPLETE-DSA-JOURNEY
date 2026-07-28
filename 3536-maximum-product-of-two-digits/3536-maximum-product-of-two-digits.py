class Solution:
    def maxProduct(self, n: int) -> int:
        newlist=[]
        total = 0
        while(n!=0):
            total = n%10
            n=n//10
            newlist.append(total)
        newlist.sort()
        return newlist[-1]*newlist[-2]



        