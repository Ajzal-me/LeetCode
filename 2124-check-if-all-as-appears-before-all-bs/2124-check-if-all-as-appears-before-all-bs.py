class Solution:
    def checkString(self, s: str) -> bool:
        
        if len(s) == 1:
            return True
        
        if 'b' not in s or 'a' not in s:
            return True

        for i in range(s.index('b'),len(s)):
            if s[i] == 'a':
                return False
            
        return True

        
