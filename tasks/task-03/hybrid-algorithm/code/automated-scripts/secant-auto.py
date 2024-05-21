import time
import pandas as pd  # Import pandas library
import os
import math

# Define the secant function


def secant(f, x0, x1, tol=(10**(-14)), max_iter=1000):
    # Initialize an iteration counter
    i = 0
    # Repeat until the tolerance is met or the maximum number of iterations is reached
    while abs(x1 - x0) > tol and i < max_iter:
        # Compute the function values at the current points
        f_x0 = f(x0)
        f_x1 = f(x1)
        # Calculate the new point using the secant method formula
        x2 = x1 - f_x1 * (x1 - x0) / (f_x1 - f_x0)
        # Update the points for the next iteration
        x0, x1 = x1, x2
        i += 1
    return x1, f(x1), i, x0, x1


# Read the file and store the equations and the intervals in two lists
functions = []
intervals = []
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, 'functions.txt')
with open(file_path, 'r') as file:
    for line in file:
        equation, a, b = line.split(',')  # Split the line by commas
        # Convert the equation to a lambda function and append to the list
        functions.append(eval(f'lambda x: {equation}'))
        # Convert the bounds to floats and append to the list
        intervals.append([float(a), float(b)])

# Define the number of runs for each function
num_runs = 500

# Create a list of tuples containing the function, the interval, and the average time
results = []
for i in range(len(functions)):
    f = functions[i]  # Get the function from the list
    # Get the interval from the list and use different variables
    x0, x1 = intervals[i]
    total_time = 0
    for j in range(num_runs):
        start_time = time.time()
        # Use the new variables as arguments
        result, fx, iter, a, b = secant(f, x0, x1)
        end_time = time.time()
        run_time = end_time - start_time
        total_time += run_time
    average_time = total_time / num_runs
    # Use the new variables in the list
    results.append((f, [x0, x1], average_time))

# Create a pandas dataframe from the results list
df = pd.DataFrame(results, columns=['Function', 'Interval', 'Avg CPU Time'])

# Add columns for the root, the function value, the iterations, the lower bound, and the upper bound
df['Root'] = df.apply(lambda row: secant(
    row['Function'], row['Interval'][0], row['Interval'][1])[0], axis=1)
df['f(x)'] = df.apply(lambda row: secant(row['Function'],
                                         row['Interval'][0], row['Interval'][1])[1], axis=1)
df['Iter'] = df.apply(lambda row: secant(
    row['Function'], row['Interval'][0], row['Interval'][1])[2], axis=1)
# Add the lower bound column
df['a'] = df.apply(lambda row: secant(
    row['Function'], row['Interval'][0], row['Interval'][1])[3], axis=1)
# Add the upper bound column
df['b'] = df.apply(lambda row: secant(
    row['Function'], row['Interval'][0], row['Interval'][1])[4], axis=1)

# Drop the function and interval columns
df = df.drop(['Function', 'Interval'], axis=1)

# Add the problem column with labels
df['Problem'] = [f'$P_{{{i+1}}}$' for i in range(len(functions))]

# Reorder the columns
df = df[['Problem', 'Iter', 'Avg CPU Time', 'Root', 'f(x)', 'a', 'b']]

# Rename the columns
df = df.rename(columns={'Root': 'Approximate Root',
               'f(x)': 'Function Value', 'a': 'Lower Bound', 'b': 'Upper Bound'})

# Use the scientific notation format for the Avg CPU Time column
pd.options.display.float_format = ' {:.16f}'.format

# Save the dataframe to an excel file with the name secant-table.csv
# Use the float_format argument to set the precision of the numbers in the excel file
df.to_csv(os.path.join(script_dir, '../results/secant-table.csv'), index=False)
