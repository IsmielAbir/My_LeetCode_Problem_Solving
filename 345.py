class Solution:
    def reverseVowels(self, s: str) -> str:
        j = 0
        li = []
        for i in range(len(s)):
            if (s[i]=='a' or s[i]=='e' or s[i]=='i' or s[i]=='o' or s[i]=='u' or s[i]=='A' or s[i]=='E' or s[i]=='I' or s[i]=='O' or s[i]=='U'):
                li.append(s[i])
        p = ''.join(li)[::-1]

        u = ''
        for i in range(len(s)):
            if (s[i]=='a' or s[i]=='e' or s[i]=='i' or s[i]=='o' or s[i]=='u' or s[i]=='A' or s[i]=='E' or s[i]=='I' or s[i]=='O' or s[i]=='U'):
                u+=p[j]
                j+=1
            else:
                u+=s[i]
        return u
