#User function Template for python3

class Solution:
	def nthStair(self,n):
		# Code here
		if n<=1:
		    return n 
		l=[0]*n
		l[0]=1
		for i in range(1,n):
		    if i%2!=0:
		        l[i]=l[i-1]+1
		    else:
		        l[i]=l[i-1]
		return l[-1]
