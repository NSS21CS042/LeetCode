class Solution:
    def makeFancyString(self, s: str) -> str:
        result=''
        for i in s:
            if not result[-2:] == i*2:
                result+=i
        return result