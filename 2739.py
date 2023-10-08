class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        count = 0
        while(mainTank>=5 and additionalTank>0 ):
            mainTank = (mainTank-5)
            additionalTank-=1
            count+=5
            mainTank+=1
        return(count+mainTank)*10
        
