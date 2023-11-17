#!/bin/python3

class Solution:

    def lengthOfLongestSubstring(self, s):

        if len(s)==0:
            return 0
        
        accumSet=set()
        maxLen=0
        currLen=0
        startIdx=-1
        endIdx=-1
        
        
        while True:
          
            isDuplicate=False
          
            while endIdx<len(s)-1:
                endIdx+=1
                endChar=s[endIdx]
                 
                if endChar not in accumSet:
                    accumSet.add(endChar)
                    
                    # Здесь запоминается максимальная длинна участка
                    currLen=endIdx-startIdx
                    if currLen>maxLen:
                        maxLen=currLen
                        print("maxLen: "+str(maxLen))
                    
                else:
                    isDuplicate=True
                    break
                   
           
            if isDuplicate:
              
                while startIdx<len(s)-1:
                    startIdx+=1
                    startChar=s[startIdx]
                    
                    if startChar!=s[endIdx]:
                        accumSet.discard(startChar)
                        continue
                    else:
                        break
                
            if endIdx>=len(s)-1:
                break

        
        return maxLen
             
        
'''
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
'''      
      
solutin=Solution()

s="abcabcbb"
# s="bbbbb"
# s="pwwkew"
# s=" "
print(s)
i=solutin.lengthOfLongestSubstring(s)

print(i)
