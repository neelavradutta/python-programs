class Solution:
    def longestPrefix(self, s: str) -> str:
        pre=[]
        suf=[]
        final=[]
        for i in range(len(s)-1):
            pre.append(s[:i+1])

        
        for i in range(len(s)-1,0,-1):
            suf.append(s[i:])
        

        for i in range(len(pre)):
            if pre[i] in suf:
                final.append(pre[i])
                
        if len(final)>0:
            return final[-1]
        else:
            return ""



        