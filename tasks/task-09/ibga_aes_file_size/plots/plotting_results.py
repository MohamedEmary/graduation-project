import scienceplots
import pandas as pd
import matplotlib.pylab as plt
import os

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
    aes_different_sizes_enc = df['aes_different_sizes_enc'].dropna().tolist()
    aes_different_sizes_dec = df['aes_different_sizes_dec'].dropna().tolist()
    aes_different_sizes_total = df['aes_different_sizes_total'].dropna(
    ).tolist()
    aes_different_keys_enc = df['aes_different_keys_enc'].dropna().tolist()
    aes_different_keys_dec = df['aes_different_keys_dec'].dropna().tolist()
    aes_different_keys_total = df['aes_different_keys_total'].dropna().tolist()
    degrees = df['degrees'].dropna().tolist()
    key_sizes = df['key_sizes'].dropna().tolist()
    polynomials_degrees = df['polynomials_degrees'].dropna().tolist()

# ================================================================================================================================================

# Plotting Results:

# ===========================Different Text Size===========================

# Encryption Time Comparison
plt.figure(figsize=(18, 6))
plt.plot(text_sizes, secant_different_sizes_enc, label='IBGA (Secant)')
plt.plot(text_sizes, aes_different_sizes_enc, label='AES')
plt.xlabel('File Size')
plt.ylabel('Encryption Time')
plt.title('Encryption Time with Different File Sizes for IBGA (Secant) vs AES')
plt.legend()
plt.savefig(os.path.join(
    script_dir, "./encryption_time_comparison.svg"), format="svg")
# plt.show()

# Decryption Time Comparison
plt.figure(figsize=(18, 6))
plt.plot(text_sizes, secant_different_sizes_dec, label='IBGA (Secant)')
plt.plot(text_sizes, aes_different_sizes_dec, label='AES')
plt.xlabel('File Size')
plt.ylabel('Decryption Time')
plt.title('Decryption Time with Different File Sizes for IBGA (Secant) vs AES')
plt.legend()
plt.savefig(os.path.join(
    script_dir, "./decryption_time_comparison.svg"), format="svg")
# plt.show()

# Total Time Comparison
plt.figure(figsize=(18, 6))
plt.plot(text_sizes, secant_different_sizes_total, label='IBGA (Secant)')
plt.plot(text_sizes, aes_different_sizes_total, label='AES')
plt.xlabel('File Size')
plt.ylabel('Total Time')
plt.title('Total Time with Different File Sizes for IBGA (Secant) vs AES')
plt.legend()
plt.savefig(os.path.join(
    script_dir, "./total_time_comparison.svg"), format="svg")
# plt.show()

# ===========================Different Key Size & Polynomial Degree===========================

# Encryption Time Comparison
plt.figure(figsize=(18, 6))
plt.plot(polynomials_degrees, secant_different_deg_enc, label='IBGA (Secant)')
plt.plot(polynomials_degrees, aes_different_keys_enc, label='AES')
plt.xlabel('Polynomial Degree & Key Size')
plt.ylabel('Encryption Time')
plt.title(
    'Encryption Time with Different Polynomial Degrees for IBGA (Secant) vs AES')
plt.legend()
x_labels = [f"({int(deg)} Deg, {int(key)} Chars)" for deg,
            key in zip(degrees, key_sizes)]
plt.xticks(polynomials_degrees, x_labels)
plt.savefig(os.path.join(
    script_dir, "./encryption_time_comparison_deg.svg"), format="svg")
# plt.show()

# Decryption Time Comparison
plt.figure(figsize=(18, 6))
plt.plot(polynomials_degrees, secant_different_deg_dec, label='IBGA (Secant)')
plt.plot(polynomials_degrees, aes_different_keys_dec, label='AES')
plt.xlabel('Polynomial Degree & Key Size')
plt.ylabel('Decryption Time')
plt.title(
    'Decryption Time with Different Polynomial Degrees for IBGA (Secant) vs AES')
plt.legend()
x_labels = [f"({int(deg)} Deg, {int(key)} Chars)" for deg,
            key in zip(degrees, key_sizes)]
plt.xticks(polynomials_degrees, x_labels)
plt.savefig(os.path.join(
    script_dir, "./decryption_time_comparison_deg.svg"), format="svg")
# plt.show()

# Total Time Comparison
plt.figure(figsize=(18, 6))
plt.plot(polynomials_degrees, secant_different_deg_total, label='IBGA (Secant)')
plt.plot(polynomials_degrees, aes_different_keys_total, label='AES')
plt.xlabel('Polynomial Degree & Key Size')
plt.ylabel('Total Time')
plt.title('Total Time with Different Polynomial Degrees for IBGA (Secant) vs AES')
plt.legend()
x_labels = [f"({int(deg)} Deg, {int(key)} Chars)" for deg,
            key in zip(degrees, key_sizes)]
plt.xticks(polynomials_degrees, x_labels)
plt.savefig(os.path.join(
    script_dir, "./total_time_comparison_deg.svg"), format="svg")
# plt.show()
