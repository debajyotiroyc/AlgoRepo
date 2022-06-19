class Solution:
    def majorityElement(self, A, N):
        #Your code here
        freq=dict()
        
        for i in A:
            freq[i]=freq.get(i,0)+1
        for i in freq:
            if freq[i]>N//2:
                return i
        return -1