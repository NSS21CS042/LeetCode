class Solution(object):
    def decrypt(self, code, k):
        """
        :type code: List[int]
        :type k: int
        :rtype: List[int]
        """
        n=len(code)
        result=[]
        if k==0:
            for i in range(n):
                result.append(0)
        elif k>0:
            for i in range(n):
                sum1=0
                j=1
                while(j<=k):
                    sum1+=code[(i+j)%n]
                    j+=1
                result.append(sum1)
        else:
            for i in range(n):
                sum1=0
                j=i-abs(k)
                while(j<=i-1):
                    sum1+=code[(j+n)%n]
                    j+=1
                result.append(sum1)
        return result