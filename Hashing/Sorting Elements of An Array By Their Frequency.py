class Solution:
   
    #Function to sort the array according to frequency of elements.
    def sortByFreq(self,a,n):
        #code here
        freq=dict()
        for i in a:
            freq[i]=freq.get(i,0)+1
        a.sort()
        a.sort(key=lambda x:freq[x],reverse =True)
        return a