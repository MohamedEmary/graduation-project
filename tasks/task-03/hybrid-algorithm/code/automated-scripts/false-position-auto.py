import math
import time
import pandas as pd
import os


# Define the false position function
def falsePosition(f, x0, x1, e=(10**(-14))):
    step = 1
    condition = True
    while condition:
        x2 = x0 - (x1-x0) * f(x0)/(f(x1) - f(x0))
        if f(x0) * f(x2) < 0:
            x1 = x2
        else:
            x0 = x2
        step += 1
        condition = abs(f(x2)) > e

    return x2, f(x2), step, x0, x1


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

# Create a list of tuples containing the function, the interval, and the average time for the false position method
results = []
for i in range(len(functions)):
    f = functions[i]  # Get the function from the list
    # Get the interval from the list and use different variables
    a1, b1 = intervals[i]
    total_time = 0
    for j in range(num_runs):
        start_time = time.time()
        # Use the new variables as arguments
        result, fx, iter, x0, x1 = falsePosition(f, a1, b1)
        end_time = time.time()
        run_time = end_time - start_time
        total_time += run_time

    average_time = total_time / num_runs
    # Use the new variables in the list
    results.append((f, [a1, b1], average_time))

# Create a pandas dataframe from the results list
df = pd.DataFrame(results, columns=['Function', 'Interval', 'Avg CPU Time'])

# Add columns for the root, the function value, the iterations, the lower bound, and the upper bound, using the falsePosition function
df['Root'] = df.apply(lambda row: falsePosition(
    row['Function'], row['Interval'][0], row['Interval'][1])[0], axis=1)
df['f(x)'] = df.apply(lambda row: falsePosition(
    row['Function'], row['Interval'][0], row['Interval'][1])[1], axis=1)
df['Iter'] = df.apply(lambda row: falsePosition(
    row['Function'], row['Interval'][0], row['Interval'][1])[2], axis=1)
# Add the lower bound column
df['a'] = df.apply(lambda row: falsePosition(
    row['Function'], row['Interval'][0], row['Interval'][1])[3], axis=1)
# Add the upper bound column
df['b'] = df.apply(lambda row: falsePosition(
    row['Function'], row['Interval'][0], row['Interval'][1])[4], axis=1)

# Drop the function and interval columns
df = df.drop(['Function', 'Interval'], axis=1)

# Add the problem column with labels
df['Problem'] = [f'$P{i+1}$' for i in range(len(functions))]

# Reorder the columns
# Include the lower and upper bound columns
df = df[['Problem', 'Iter', 'Avg CPU Time', 'Root', 'f(x)', 'a', 'b']]

# Rename the columns
df = df.rename(columns={'Root': 'Approximate Root',
               'f(x)': 'Function Value', 'a': 'Lower Bound', 'b': 'Upper Bound'})

# Use the scientific notation format for the Avg CPU Time column
pd.options.display.float_format = ' {:.16f}'.format

# Save the dataframe to an excel file with a different name, such as false-position-table.xlsx
df.to_csv(os.path.join(script_dir, '../results/false-position-table.csv'), index=False)
