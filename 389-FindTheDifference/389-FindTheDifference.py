# Last updated: 7/18/2026, 8:31:44 PM

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        count_s = Counter(s)
        count_t = Counter(t)

        for char, count in count_t.items():
            print(char)
            print(count)
            if char not in count_s or count > count_s[char]:
                return char
        
            