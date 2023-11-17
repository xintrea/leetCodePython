#!/bin/python3

class Solution:

    # Функция возвращает символ, который расположен в указанных координатах
    # при заданной текстовой строке и количестве вертикальных строк
    # Не написал
   
    # Функция возвращает координаты указанного по номеру символа
    def getXYbyNum(self, s, numRows, n):
        # Выясняется период зигзага в символах
        pChar=2*(numRows-1)

        # Выясняется период зигзага по оси X
        pX=numRows-1

        # Остаток от деления на период в символах покажет какой номер символа в первой "галке"
        nCharInV=n % pChar

        # Вычисляются координаты в первой "галке"
        if nCharInV<=pChar//2:
            fX=0
            fY=nCharInV
        else:
            fX=nCharInV-pChar//2
            fY=pChar-nCharInV

        # Номер "галки", в которой находится символ
        numV=n // pChar

        fX=numV*pX+fX

        return fX, fY


    def hashXY(self, x: int, y: int) -> int:
        tmp = ( y +  ((x+1)/2))
        return x +  ( tmp * tmp)


    def convert(self, s: str, numRows: int) -> str:

        if numRows==1:
            return s

        # Перечень координат всех символов
        xy={}
        for n in range(0, len(s)):
            # x, y = self.getXYbyNum(s, numRows, n)
            xy[ self.hashXY( *self.getXYbyNum(s, numRows, n) ) ]=s[n]

        # Ширина рисунка
        width=self.getXYbyNum(s, numRows, len(s)-1)[0]
        
        print(f"Width: {width}")

        result=""

        for y in range(0, numRows):
            for x in range(0, width+1):
                hash=self.hashXY(x, y)
                if hash in xy:
                    result+=(xy[hash])

        return result


solution=Solution()

data=[]
data.append( ("A", 1) )
data.append( ("ALPHABETICALSTRING", 4) )
data.append( ("PAYPALISHIRING", 3) )
data.append( ("PAYPALISHIRING", 4) )

for element in data:
    s, n = element
    print(f"Given: {s} {n}")
    result=solution.convert(s, n)
    print("Result: "+result)    

