def numberOfCuts(self, n: int) -> int:
        if(n>1 and n%2!=0):
            return n
        elif(n>1 and n%2==0):
            return n//2
        else:
            return 0