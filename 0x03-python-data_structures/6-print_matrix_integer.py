#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in range(len(matrix)):
        val = matrix[i]
        for j in range(len(matrix[i])):
            print("{:d}".format(val[j]), end=" " if len(val)-1 != j else "")
        print("")
