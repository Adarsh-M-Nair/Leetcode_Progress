# Last updated: 7/18/2026, 8:31:49 PM
class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels=set('AEIOUaeiou')
        l=list(s)
        i=0
        j=len(s)-1
        while(i<j):
            while i<j and l[i] not in vowels:
                i+=1
            while i<j and l[j] not in vowels:
                j-=1
            if i<j:
                l[i],l[j]=l[j],l[i]
                i+=1
                j-=1
           
        return "".join(l)    