---
title: \huge Dataset Columns
date: \today
---

# What does each column represent

| Column           | Description                                                                                                |
| ---------------- | ---------------------------------------------------------------------------------------------------------- |
| `x`              | sorted interval from 0 to 99 [inclusive]                                                                   |
| `y`              | positive and negative from 1 to 99 [inclusive]. We start from 1 to avoid 0 [-y,+y] ex: [-3,3]              |
| `random_state`   | random seed generator from 0 to 99 [inclusive]                                                             |
| `sections`       | random odd number from 3 to 15 [inclusive]                                                                 |
| `random_mat_row` | get the row from `random_matrix.csv`                                                                       |
| `x_points`       | split x interval evenly into `sections`                                                                    |
| `y_points`       | split y interval evenly into `sections`                                                                    |
| `rand_vals`      | `section+1` values from `random_mat_row`                                                                     |
| `points`         | zip `x_points` and `y_points`                                                                              |
| `poly_points`    | change `y_points` by adding then subtracting a random value from `rand_vals` to each element in `y_points` |
| `polynomial`     | get the polynomial function from `poly_points` using lagrange interpolation                                |
| `rand_text`      | random text samples with length `text_size`                                                                |
| `random_mat`     | is a random matrix generated in `random_matrix.py` file                                                    |
