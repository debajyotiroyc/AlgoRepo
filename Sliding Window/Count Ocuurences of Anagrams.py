#User function Template for python3
class Solution:
	def search(self,pat, txt):
	    # code here
	   f1=dict()
	   for i in pat:
	       f1[i]=f1.get(i,0)+1
	   f2=dict()
	   c,k=0,len(pat)
	   for i in range(0,k):
	       f2[txt[i]]=f2.get(txt[i],0)+1
	   if f2==f1:
	       c=c+1
	   for i in range(k,len(txt)):
	       f2[txt[i-k]]=f2.get(txt[i-k],0)-1
	       if f2[txt[i-k]]<=0:
	           f2.pop(txt[i-k])
	       f2[txt[i]]=f2.get(txt[i],0)+1
	       if f2==f1:
	           c=c+1
	   return c
	   