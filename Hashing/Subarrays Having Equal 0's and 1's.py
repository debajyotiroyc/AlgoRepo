class Solution:
    
    #Function to count subarrays with 1s and 0s.
    def countSubarrWithEqualZeroAndOne(self,arr, n):
        #Your code here
        s,c=0,0
        freq=dict()
        for i in range(n):
            if arr[i]==0:
                s=s+(-1)
            else:
                s=s+1
            if s==0:
                c=c+1
            
            if s in freq:
                c=c+freq[s]
            freq[s]=freq.get(s,0)+1
        return c
