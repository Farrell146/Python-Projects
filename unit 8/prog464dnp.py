import pandas as pd
import numpy as np

def main():
    mat=pd.read_csv("data/prog464a.dat",sep=" ",header=None)
    mat=np.array(mat)
    print(mat)

    print("Transposed")
    print(mat.T) #.T is a shorthand for .transposed. this is a numpy function

if __name__ == "__main__":
  main()