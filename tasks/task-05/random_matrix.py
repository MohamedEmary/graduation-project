import numpy as np
import pandas as pd


def random_matrix(rows_num, vals):
    return [np.random.randint(start, end, vals) for _ in range(rows_num)]


start = 1000000
end = 1000100
top_power = 14
matrix_samples = 100

mat = random_matrix(matrix_samples, top_power)
column_names = [str(i) for i in range(top_power)]
pd.DataFrame(mat, columns=column_names).to_csv(
    "random_matrix.csv", header=True, index=None, sep=',')
