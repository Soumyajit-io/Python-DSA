class Solution(object):
    def removeDuplicates(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        l = [s[0]]
        for i in range(1,n):
            if len(l)!=0 and s[i]==l[-1]:
                l.pop()
            else:
                l.append(s[i])
        
        s=""
        for i in l:
            s+=str(i)

        return s
