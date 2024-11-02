class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        words=sentence.split()
        n=len(words)
        f=0
        for i in range(n):
            first=words[i]
            m=i+1
            second=words[m%n]
            if first[-1] == second[0]:
                f=1
            else:
                return False
        if f==1:
            return True