import math
import time
import pandas as pd
import os


def blendSF(f, a, b, eps=10**(-14)):
    n = 0

    while True:
        n += 1

        fa = f(a)
        fb = f(b)

        x_val = a - (fa * (b - a)) / (fb - fa)
        fx = f(x_val)

        if abs(fx) <= eps:
            return x_val, fx, n, a, b
        else:
            aS = b
            bS = x_val

            faS = fb
            fbS = fx

            xS = bS - fbS * (bS - aS) / (fbS - faS)
            fxS = f(xS)

            if abs(fxS) < abs(fx) and a < xS < b:
                if fa * fxS < 0:
                    b = xS
                else:
                    a = xS
            else:
                if fa * fx < 0:
                    b = x_val
                else:
                    a = x_val


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

# Create a list of tuples containing the function, the interval, and the average time for the hybrid algorithm
results = []
for i in range(len(functions)):
    f = functions[i]  # Get the function from the list
    # Get the interval from the list and use different variables
    a1, b1 = intervals[i]
    total_time = 0
    for j in range(num_runs):
        start_time = time.time()
        # Use the new variables as arguments
        result, fx, iter, x0, x1 = blendSF(f, a1, b1)
        end_time = time.time()
        run_time = end_time - start_time
        total_time += run_time

    average_time = total_time / num_runs
    # Use the new variables in the list
    results.append((f, [a1, b1], average_time))

# Create a pandas dataframe from the results list
df = pd.DataFrame(results, columns=['Function', 'Interval', 'Avg CPU Time'])

# Add columns for the root, the function value, the iterations, the lower bound, and the upper bound, using the blendSF function
df['Root'] = df.apply(lambda row: blendSF(
    row['Function'], row['Interval'][0], row['Interval'][1])[0], axis=1)
df['f(x)'] = df.apply(lambda row: blendSF(row['Function'],
                                          row['Interval'][0], row['Interval'][1])[1], axis=1)
df['Iter'] = df.apply(lambda row: blendSF(
    row['Function'], row['Interval'][0], row['Interval'][1])[2], axis=1)
# Add the lower bound column
df['a'] = df.apply(lambda row: blendSF(
    row['Function'], row['Interval'][0], row['Interval'][1])[3], axis=1)
# Add the upper bound column
df['b'] = df.apply(lambda row: blendSF(
    row['Function'], row['Interval'][0], row['Interval'][1])[4], axis=1)

# Drop the function and interval columns
df = df.drop(['Function', 'Interval'], axis=1)

# Add the problem column with labels
df['Problem'] = [f'$P_{{{i+1}}}$' for i in range(len(functions))]

# Reorder the columns
# Include the lower and upper bound columns
df = df[['Problem', 'Iter', 'Avg CPU Time', 'Root', 'f(x)', 'a', 'b']]

# Rename the columns
df = df.rename(columns={'Root': 'Approximate Root',
               'f(x)': 'Function Value', 'a': 'Lower Bound', 'b': 'Upper Bound'})

# Use the scientific notation format for the Avg CPU Time column
pd.options.display.float_format = ' {:.16f}'.format

# Save the dataframe to an excel file with a different name, such as hybrid-table.xlsx
df.to_csv(os.path.join(script_dir, '../results/hybridSF-table.csv'), index=False)
