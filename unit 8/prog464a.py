import pandas as pd
import numpy as np

def main():
    mat=pd.read_csv("data/prog464a.dat",sep=" ",header=None)
    mat=np.array(mat)

    #making a 0 column of all zeros, in order to make a 6th column
    zerocolumn=np.zeros((5,1)) #zeros function takes in a tuple
    matrix=np.append(mat,zerocolumn,axis=1).astype(int) #1=y-axis, 0=x-axis

    #iterate through every single row to find the max num

    for r in range(len(matrix)):
        currentmax=matrix[r][0]
        for c in range(len(matrix[r])-1):
           if matrix[r][c]>currentmax:
              currentmax=matrix[r][c]
        matrix[r][len(matrix[r])-1]=currentmax
        #matrix[r][len(matrix[r])-1]=max(matrix[r]) -- no need for a second for loop

    print(matrix)

if __name__ == "__main__":
  main()

"""
[[45 67 89 12 -3 89]
 [-3 -6 -7 -4 -9 -3]
 [96 81 -8 52 12 96]
 [14 -7 72 29 -1 72]
 [19 43 28 63 87 87]]
"""