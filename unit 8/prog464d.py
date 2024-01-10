def main():
  try:
    with open("data/prog464a.dat", 'r') as f:
        matrix=[]

        for line in f:
            intline=[int(x) for x in line.split()]
            matrix.append(intline)

        for r in range(len(matrix)):
          for c in range(len(matrix[r])):
             print(matrix[r][c],end=' ')
          print()

        def matrixtranspose(mat):
          transpose=[]
          for r in range(len(mat)):
            transpose.append([0]*len(mat[r])) #adds empty row
          for r in range(len(mat)):
            for c in range(len(mat[r])):
               transpose[c][r]=mat[r][c]
          return transpose
        
        print("Transposed Matrix:")
        matrixt=matrixtranspose(matrix)

        for r in range(len(matrixt)):
          for c in range(len(matrixt[r])):
             print(matrixt[r][c],end=' ')
          print()

        
        
  except Exception as z:
    print("Error:", z)

if __name__ == "__main__":
  main()


"""
45 67 89 12 -3 
-3 -6 -7 -4 -9
96 81 -8 52 12
14 -7 72 29 -1
19 43 28 63 87
Transposed Matrix:
45 -3 96 14 19
67 -6 81 -7 43
89 -7 -8 72 28
12 -4 52 29 63
-3 -9 12 -1 87
"""