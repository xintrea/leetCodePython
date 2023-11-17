#!/bin/python3

class Solution:

    def longestPalindrome(self, s: str) -> str:
        if len(s)<=1:
            return s
        
        if len(s)==2:
            if s[0:1]==s[1:2]:
                return s
            else:
                return s[0:1]

        maxLen=0
        maxPal=""

        # Проверяются палиндромы, начиная с пары символов
        for i in range(0, len(s)-1):
            for j in range(i+1, len(s)):
                p=s[i:j+1] # Проверяемая подстрока
                # print("Curr: "+p+" From: "+str(i)+" To: "+str(j))
                divPoint=len(p)//2
                if len(p)>maxLen and p[0:divPoint]==p[-1:-divPoint-1:-1]:
                    maxLen=len(p)
                    maxPal=p

                if (len(s)-i)<maxLen:
                    return maxPal

        # Если палиндром в парах не найден, возвращается первый символ 
        # так как он и есть палиндром, а длина входной строки здесь от трех и выше
        if len(maxPal)==0:
            return s[0:1]
        else:
            return maxPal
          
      
solutin=Solution()

data=[]
data.append("abacab")
data.append("abcda")
data.append("ccc")
data.append("abb")
data.append("a")
data.append("ac")
data.append("aca")
data.append("affa")
data.append("babad")
data.append("cbbd")
data.append("abcabcbb")
data.append("bbbbb")
data.append("pwwkew")
data.append("abcabcbca")


for s in data:
    print("Given: "+s)
    result=solutin.longestPalindrome(s)
    print(result)

