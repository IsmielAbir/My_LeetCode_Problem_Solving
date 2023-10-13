class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        c=0
        d = 0
        a = (bin(n)[2:])[::-1]
        for i in range(len(a)):
            if i%2==0:
                if a[i]=='1':
                    c+=1
            else:
                if a[i]=='1':
                    d+=1

                
        return [c,d]
       