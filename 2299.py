class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        u,l,d,s=0,0,0,0
        if len(password)<8: return False
        for i in range(0,len(password)):
            if i>0 and password[i-1]==password[i]: return False
            if password[i].isdigit(): d+=1
            elif password[i].islower(): l+=1
            elif password[i].isupper(): u+=1
            elif password[i] in "!@#$%^&*()-+": s+=1
        if u!=0 and l!=0 and d!=0 and s!=0: return True