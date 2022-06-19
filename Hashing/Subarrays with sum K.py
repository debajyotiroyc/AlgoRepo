class Solution:
    def findSubArraySum(self, Arr, N, k):
        # code here
        s,c=0,0
        freq=dict()
        for i in range(N):
            #print(s,freq,c)
            s=s+Arr[i]
            if s==k:
                c=c+1
            
            if (s-k) in freq:
                c=c+freq[s-k]
            
            freq[s]=freq.get(s,0)+1
        return c