import os

class Echelon:
    def __init__(self, matrix) -> None:
        self.matrix = matrix
    
    def zero_care(self):
        def sorter(n):                      #sort according to zeroes in the beginning
            k = 0
            m = 0
            for i in n:
                if k==m:
                    if i==0:
                        k+=1
                else:
                    break
                m+=1
            return k

        def sort_asc(n):                #sort according to the first element
            return n[0]

        nm = list()
        k = len(self.matrix)
        m=0
        while m<k:
            if self.matrix[m][0]==0:
                nm.append(self.matrix[m])
                self.matrix.pop(m)              #pop rows with zero in the beginning
                m-=1
                k-=1
            m+=1
        self.matrix.sort(key=sort_asc)
        nm.sort(key=sorter)
        for x in nm:
            self.matrix.append(x)           #add rows with zeroes back
        self.print_arr()

    def check_zeroes(self,row):
        i=0
        n = 0
        for x in row:
            if x==0:
                n+=1
            else:
               break
        return n

    def print_arr(self):
        l = 0
        for x in self.matrix:
            for y in x:
                if len(str(y))>l:
                    l = len(str(y))
        digits = l
        for x in self.matrix:
            for y in x:
                if y == 0.0 or -0.0:
                    y = int(y)
                print(format(str(y), f"<{str(digits+5)}"), end="")
            print()
        print("\n")

    def convert_row_echelon(self):
        n = 0
        while n < len(self.matrix):
            zeroes = self.check_zeroes(self.matrix[n])
            i = n+1
            while i < len(self.matrix):
                new_zeroes = self.check_zeroes(self.matrix[i])
                if new_zeroes < zeroes+1 and zeroes<len(self.matrix[n]):
                    multiplier = self.matrix[n][zeroes]/self.matrix[i][zeroes]
                    print(f"(R{str(i+1)} = {multiplier}xR{str(i+1)} - R{str(n+1)})")
                    for a in range(len(self.matrix[i])):
                        self.matrix[i][a] = self.matrix[i][a]*multiplier - self.matrix[n][a]
                    self.print_arr()
                i+=1
            n+=1

    def convert_reduced_row_echelon(self):
        n = 0
        while n<len(self.matrix):
            m = 0
            z = self.check_zeroes(self.matrix[n])
            if (z<len(self.matrix[n])):
                a = self.matrix[n][z]
                while m<len(self.matrix[n]):
                    self.matrix[n][m] = self.matrix[n][m]/a
                    m+=1
            n+=1
        self.print_arr()
                    
