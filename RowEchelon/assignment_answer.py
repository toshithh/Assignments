import os
from echelon import *

matrix = [[0,0,0,0],
          [-2,-4,2,2],
          [3,6,-3,-3],
          [1,2,0,1]
         ]
ans = Echelon(matrix)
os.system("cls")
print("Initial Array:")
ans.print_arr()
ans.zero_care()
ans.convert_row_echelon()
ans.convert_reduced_row_echelon()
ans.zero_care()