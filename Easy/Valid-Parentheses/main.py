class Solution:
    def isValid(self, s: str) -> bool:
        if(len(s)%2!=0):
            return False

        
        a  = [0 for x in range(len(s))]
        for x in range(len(s)):
            a[x] = ord(s[x])

        while(len(a)>1):
            c = len(a)
            for x in range(len(a)-1):
                if(a[x+1]-a[x] == 1 or a[x+1]-a[x] == 2 ):
                    del a[x]
                    del a[x]
                    x = x-2
                    break
            if(len(a) == c):
                
                break


   
        if(len(a) == 0):
            return True

        else:
            return False

#Performance
# Runtime (ms): 1180
# Memory Usage: 13.8 MB