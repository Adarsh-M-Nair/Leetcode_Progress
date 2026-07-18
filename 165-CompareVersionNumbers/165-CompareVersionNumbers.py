# Last updated: 7/18/2026, 8:32:20 PM
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        l1 = list(map(int, version1.split(".")))
        l2 = list(map(int, version2.split(".")))
        
        len1, len2 = len(l1), len(l2)
        length = max(len1, len2)
        
        for i in range(length):
            v1 = l1[i] if i < len1 else 0
            v2 = l2[i] if i < len2 else 0
            
            if v1 < v2:
                return -1
            elif v1 > v2:
                return 1
        
        return 0