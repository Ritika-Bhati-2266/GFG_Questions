#User function Template for python3
class Solution:
    def evenlyDivides(self, n):
        # code here
        num = n
        count = 0
        while num > 0:
            l = num % 10
            if l!=0 and n%l==0:
                count = count+1
            num = num//10
        return count