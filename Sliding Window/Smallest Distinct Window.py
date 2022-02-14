#User function Template for python3

class Solution:
    def findSubString(self, s):
        # Your code goes here
        freq=dict()
        s1=set(s)
        for i in s1:
            freq[i]=-1
        c,m=0,len(s)*2
        for i in range(len(s)):
            freq[s[i]]=i
            #print(freq)
            mi=min(freq.values())
            if mi==-1:
                continue
            mx=max(freq.values())
            m = min(m,mx-mi+1)
        return m
        