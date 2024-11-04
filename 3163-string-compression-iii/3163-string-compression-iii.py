class Solution:
    def compressedString(self, word: str) -> str:
        comp=[]
        pos=0
        while pos<len(word):
            count=0
            char=word[pos]
            while(pos<len(word) and count<9 and word[pos]==char):
                count+=1
                pos+=1
            comp.append(str(count))
            comp.append(char)
        comp="".join(comp)
        return comp
    