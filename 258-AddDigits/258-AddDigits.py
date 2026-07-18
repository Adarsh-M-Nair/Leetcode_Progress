# Last updated: 7/18/2026, 8:32:01 PM
class Solution:
    def addDigits(self, num: int) -> int:
        s=0
        if num<10:
            return num
        else:
            while(num>=10):
                temp=num
                s=0
                while (temp>0):
                    d=temp%10
                    s+=d
                    temp//=10
                num=s
            return s

        