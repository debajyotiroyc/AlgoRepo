class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        x=0
        l=[a,b,c]
        l.sort()
        n=0
        while n<=1:
          l[1]=l[1]-1
          l[2]=l[2]-1
          l.sort()
          n=l.count(0)
          x=x+1
        return x
            
            
            
          