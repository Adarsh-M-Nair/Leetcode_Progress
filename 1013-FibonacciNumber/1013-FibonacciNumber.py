# Last updated: 7/18/2026, 8:31:29 PM
class Solution:
    def fib(self, n: int) -> int:
        if n==0:
            return 0
        first=0
        second=1
        fibonacci=[]
        fibonacci.append(first)
        fibonacci.append(second)
        for i in range(2,n):
            third=first+second
            first=second
            second=third
            fibonacci.append(third)
        return fibonacci[n-1]+fibonacci[n-2]