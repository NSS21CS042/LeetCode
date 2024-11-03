class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        l=len(s)
        for i in range(l):
            s=s[1:]+s[0]
            if s==goal:
                return True
            
        return False