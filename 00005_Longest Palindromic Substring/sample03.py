class Solution:

    cacheOk=set()
    cacheFail=set()

    def isPalinrome(self, s: str) -> bool:
        # print("Candidate: "+s)

        # Быстрая проверка через кеш
        if s in self.cacheOk:
            return True
        if s in self.cacheFail:
            return False
        
        # Быстрая проверка через кеш - середина и крайние символы
        if len(s)>=3:
            # middleString=s[1:-1]
            # print("middleString: "+middleString)
            if s[1:-1] in self.cacheOk and s[0]==s[-1]:
                self.cacheOk.add(s)
                return True

        divPoint=len(s) // 2
        # a=s[0:divPoint]
        # b=s[-1:-divPoint-1:-1]

        if s[0:divPoint]==s[-1:-divPoint-1:-1]:
            self.cacheOk.add(s)
            return True
        else:
            if len(s)<64:
                self.cacheFail.add(s)
            return False


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

        # Проверяются подстроки-палиндромы, начиная с пары символов
        for i in range(0, len(s)-1):
            for j in range(i+1, len(s)):
                p=s[i:j+1]
                # print("Curr: "+p+" From: "+str(i)+" To: "+str(j))
                if len(p)>maxLen and self.isPalinrome(p):
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
