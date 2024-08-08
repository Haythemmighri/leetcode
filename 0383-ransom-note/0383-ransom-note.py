class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mapx = {}
        for i in magazine:
            if i not in mapx:
                mapx[i] = 1
            else:
                mapx[i] += 1
    
        for i in ransomNote:
            if i not in mapx:
                return False
            elif i in mapx:
                mapx[i] -= 1
                if mapx[i] < 0:
                    return False
        return True