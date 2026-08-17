class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        n=len(s)
        if n%2!=0: return False
        l =[]
        for i in range(n):
            if s[i]=="(" or s[i] == "{" or s[i] == "[":
                l.append(s[i])
            else:
                if len(l) ==0: return False
                x = l.pop()
                if s[i]==")" and x=="(":
                    continue
                elif s[i]=="}" and x=="{":
                    continue
                elif s[i]=="]" and x=="[":
                    continue
                else:
                    return False
        return False if l else True