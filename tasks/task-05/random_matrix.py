import numpy as np
import pandas as pd


def random_array(start, end, vals):
    res = []
    for i in range(vals):
        res.append(np.random.randint(start, end))
    return res


def random_matrix(rows_num, arr):
    mat = []
    # shuffle the values in arr to get a random matrix
    for i in range(rows_num):

        np.random.seed(i)  # set a different seed for each row
        arr_shuffled = np.random.permutation(arr)
        mat.append(list(arr_shuffled))
    return mat


numbers_arr = random_array(0, 99, 14)
mat = random_matrix(100, numbers_arr)
# save the matrix in a csv file
column_names = [str(i) for i in range(14)]
pd.DataFrame(mat, columns=column_names).to_csv(
    "random_matrix.csv", header=True, index=None, sep=',')
