class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        l1=set("qwertyuiop")
        l2=set("asdfghjkl")
        l3=set("zxcvbnm")
        result=[]
        for i in words:
            w=set(i.lower())
            if len(l1|w)==len(l1) or len(l2|w)==len(l2) or len(l3|w)==len(l3):
                result.append(i)
        return result
                
                
                    