import scienceplots
import pandas as pd
import matplotlib.pylab as plt
import os
import numpy as np

pd.set_option("display.max_rows", 50)
pd.set_option("display.max_columns", 500)
plt.rcParams.update({'font.size': 14})
plt.style.use(['science', 'no-latex'])
plt.rcParams['font.family'] = 'Times New Roman'

# Get the directory of the current script
script_dir = os.path.dirname(__file__)

# ================================================================================================================================================
# Check if results CSV exists and read it
results_csv_path = os.path.join(script_dir, 'results.csv')
if os.path.exists(results_csv_path):
    df = pd.read_csv(results_csv_path)
    text_sizes = df['text_sizes'].dropna().astype(int).tolist()
    polynomials_degrees = df['polynomials_degrees'].dropna().tolist()

    secant_different_sizes_enc = df['secant_different_sizes_enc'].dropna(
    ).tolist()
    secant_different_sizes_dec = df['secant_different_sizes_dec'].dropna(
    ).tolist()
    secant_different_sizes_total = df['secant_different_sizes_total'].dropna(
    ).tolist()
    secant_different_deg_enc = df['secant_different_deg_enc'].dropna().tolist()
    secant_different_deg_dec = df['secant_different_deg_dec'].dropna().tolist()
    secant_different_deg_total = df['secant_different_deg_total'].dropna(
    ).tolist()

    bisection_different_sizes_enc = df['bisection_different_sizes_enc'].dropna(
    ).tolist()
    bisection_different_sizes_dec = df['bisection_different_sizes_dec'].dropna(
    ).tolist()
    bisection_different_sizes_total = df['bisection_different_sizes_total'].dropna(
    ).tolist()
    bisection_different_deg_enc = df['bisection_different_deg_enc'].dropna(
    ).tolist()
    bisection_different_deg_dec = df['bisection_different_deg_dec'].dropna(
    ).tolist()
    bisection_different_deg_total = df['bisection_different_deg_total'].dropna(
    ).tolist()

    fposition_different_sizes_enc = df['fposition_different_sizes_enc'].dropna(
    ).tolist()
    fposition_different_sizes_dec = df['fposition_different_sizes_dec'].dropna(
    ).tolist()
    fposition_different_sizes_total = df['fposition_different_sizes_total'].dropna(
    ).tolist()
    fposition_different_deg_enc = df['fposition_different_deg_enc'].dropna(
    ).tolist()
    fposition_different_deg_dec = df['fposition_different_deg_dec'].dropna(
    ).tolist()
    fposition_different_deg_total = df['fposition_different_deg_total'].dropna(
    ).tolist()

    hybridbf_different_sizes_enc = df['hybridbf_different_sizes_enc'].dropna(
    ).tolist()
    hybridbf_different_sizes_dec = df['hybridbf_different_sizes_dec'].dropna(
    ).tolist()
    hybridbf_different_sizes_total = df['hybridbf_different_sizes_total'].dropna(
    ).tolist()
    hybridbf_different_deg_enc = df['hybridbf_different_deg_enc'].dropna(
    ).tolist()
    hybridbf_different_deg_dec = df['hybridbf_different_deg_dec'].dropna(
    ).tolist()
    hybridbf_different_deg_total = df['hybridbf_different_deg_total'].dropna(
    ).tolist()

    hybridsf_different_sizes_enc = df['hybridsf_different_sizes_enc'].dropna(
    ).tolist()
    hybridsf_different_sizes_dec = df['hybridsf_different_sizes_dec'].dropna(
    ).tolist()
    hybridsf_different_sizes_total = df['hybridsf_different_sizes_total'].dropna(
    ).tolist()
    hybridsf_different_deg_enc = df['hybridsf_different_deg_enc'].dropna(
    ).tolist()
    hybridsf_different_deg_dec = df['hybridsf_different_deg_dec'].dropna(
    ).tolist()
    hybridsf_different_deg_total = df['hybridsf_different_deg_total'].dropna(
    ).tolist()

# ================================================================================================================================================

# Plotting Results:


plt.figure(figsize=(18, 6))
plt.plot(polynomials_degrees,
         bisection_different_deg_enc, label='Bisection')
plt.plot(polynomials_degrees,
         fposition_different_deg_enc, label='False Position')
plt.plot(polynomials_degrees, secant_different_deg_enc,
         '-o', label='Secant')
plt.plot(polynomials_degrees,
         hybridbf_different_deg_enc, label='HybridBF')
plt.plot(polynomials_degrees,
         hybridsf_different_deg_enc, label='HybridSF')

plt.xlabel('Degree')
plt.ylabel('Encryption Time')
plt.title(
    'Encryption Time with Different Degrees for Bisection, False Position, Secant, HybridBF, HybridSF')

# Set xticks to only integer degrees
plt.xticks(np.arange(min(polynomials_degrees),
           max(polynomials_degrees)+1, 1.0))

plt.legend()
plt.savefig(os.path.join(
    script_dir, "./different_deg_enc_time.svg"), format="svg")
# plt.show()


# Encryption Time with Different File Sizes
plt.figure(figsize=(18, 6))
plt.plot(text_sizes, bisection_different_sizes_enc, label='Bisection')
plt.plot(text_sizes, fposition_different_sizes_enc,
         label='False Position')
plt.plot(text_sizes, secant_different_sizes_enc, '-o', label='Secant')
plt.plot(text_sizes, hybridbf_different_sizes_enc, label='HybridBF')
plt.plot(text_sizes, hybridsf_different_sizes_enc, label='HybridSF')

plt.xlabel('File Size')
plt.ylabel('Encryption Time')
plt.title(
    'Encryption Time with Different File Sizes for Bisection, False Position, Secant, HybridBF, HybridSF')
plt.legend()
plt.savefig(os.path.join(
    script_dir, "./different_sizes_enc_time.svg"), format="svg")
# plt.show()

# Decryption Time with Different File Sizes
plt.figure(figsize=(18, 6))
plt.plot(text_sizes, bisection_different_sizes_dec, label='Bisection')
plt.plot(text_sizes, fposition_different_sizes_dec,
         label='False Position')
plt.plot(text_sizes, secant_different_sizes_dec, '-o', label='Secant')
plt.plot(text_sizes, hybridbf_different_sizes_dec, label='HybridBF')
plt.plot(text_sizes, hybridsf_different_sizes_dec, label='HybridSF')

plt.xlabel('File Size')
plt.ylabel('Decryption Time')
plt.title(
    'Decryption Time with Different File Sizes for Bisection, False Position, Secant, HybridBF, HybridSF')
plt.legend()
plt.savefig(os.path.join(
    script_dir, "./different_sizes_dec_time.svg"), format="svg")
# plt.show()


# Decryption Time with Different Degrees
plt.figure(figsize=(18, 6))
plt.plot(polynomials_degrees,
         bisection_different_deg_dec, label='Bisection')
plt.plot(polynomials_degrees,
         fposition_different_deg_dec, label='False Position')
plt.plot(polynomials_degrees, secant_different_deg_dec,
         '-o', label='Secant')
plt.plot(polynomials_degrees,
         hybridbf_different_deg_dec, label='HybridBF')
plt.plot(polynomials_degrees,
         hybridsf_different_deg_dec, label='HybridSF')

plt.xlabel('Degree')
plt.ylabel('Decryption Time')
plt.title(
    'Decryption Time with Different Degrees for Bisection, False Position, Secant, HybridBF, HybridSF')
plt.legend()
# Set xticks to only integer degrees
plt.xticks(np.arange(min(polynomials_degrees),
           max(polynomials_degrees)+1, 1.0))

plt.savefig(os.path.join(
    script_dir, "./different_deg_dec_time.svg"), format="svg")
# plt.show()


# Total Time with Different Degrees
plt.figure(figsize=(18, 6))
plt.plot(polynomials_degrees, bisection_different_deg_total, label='Bisection')
plt.plot(polynomials_degrees,
         fposition_different_deg_total, label='False Position')
plt.plot(polynomials_degrees, secant_different_deg_total,
         '-o', label='Secant')
plt.plot(polynomials_degrees, hybridbf_different_deg_total, label='HybridBF')
plt.plot(polynomials_degrees, hybridsf_different_deg_total, label='HybridSF')

plt.xlabel('Degree')
plt.ylabel('Total Time')
plt.title('Total Time with Different Degrees for Bisection, False Position, Secant, HybridBF, HybridSF')
plt.legend()
# Set xticks to only integer degrees
plt.xticks(np.arange(min(polynomials_degrees),
           max(polynomials_degrees)+1, 1.0))

plt.savefig(os.path.join(
    script_dir, "./different_deg_total_time.svg"), format="svg")
# plt.show()


# Total Time with Different File Sizes
plt.figure(figsize=(18, 6))
plt.plot(text_sizes, bisection_different_sizes_total, label='Bisection')
plt.plot(text_sizes, fposition_different_sizes_total, label='False Position')
plt.plot(text_sizes, secant_different_sizes_total, '-o', label='Secant')
plt.plot(text_sizes, hybridbf_different_sizes_total, label='HybridBF')
plt.plot(text_sizes, hybridsf_different_sizes_total, label='HybridSF')

plt.xlabel('File Size')
plt.ylabel('Total Time')
plt.title(
    'Total Time with Different File Sizes for Bisection, False Position, Secant, HybridBF, HybridSF')
plt.legend()
plt.savefig(os.path.join(
    script_dir, "./different_sizes_total_time.svg"), format="svg")
# plt.show()
