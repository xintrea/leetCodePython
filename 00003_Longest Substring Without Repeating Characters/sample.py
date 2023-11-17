#!/bin/python3

class Solution:

    def lengthOfLongestSubstring(self, s):
        accumSet=[]
        maxLen=0
        currLen=0
        startIdx=0

        for char in s:
            print("accumSet: "+str(accumSet))
            if char not in accumSet:
                accumSet.append(char)
                currLen+=1
                if currLen>maxLen:
                    maxLen=currLen
                    print("maxLen: "+str(maxLen))
            else:

                while True:
                    startChar=s[startIdx]
                    print("startIdx: "+str(startIdx))
                    print("startChar: "+str(startChar))
                    
                    if startChar!=char:
                        accumSet.remove(startChar)
                        startIdx+=1
                    else:
                        accumSet.remove(startChar)
                        startIdx+=1
                        break

                accumSet.append(char)
                
        return maxLen
      
      
solutin=Solution()

# s="abcabcbb"
# s="bbbbb"
s="pwwkew"
print(s)
i=solutin.lengthOfLongestSubstring(s)

print(i)
