from lorem_text import lorem
import time
import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import numpy as np
from random import randint


def hybrid_method(func, a, b, tol=1e-6, max_iter=50):
    start_time = time.process_time()
    a1 = a
    a2 = a
    b1 = b
    b2 = b
    x = 0

    for i in range(max_iter):
        xT1 = (b + 2 * a) / 3
        xT2 = (2 * b + a) / 3
        xF = a - (func(a) * (b - a)) / (func(b) - func(a))
        x = xT1
        func(xT1) == func(x)

        if abs(func(xT2)) < abs(func(x)):
            x = xT2
        if abs(func(xF)) < abs(func(x)):
            x = xF
        if abs(func(x)) <= tol:
            end_time = time.process_time()
            execution_time = end_time - start_time
            return x, i, execution_time, 'hybrid_method'

        if func(a) * func(xT1) < 0:
            b1 = xT1
        elif func(xT1) * func(xT2) < 0:
            a1 = xT1
            b1 = xT2
        else:
            a1 = xT2

        if func(a) * func(xF) < 0:
            b2 = xF
        else:
            a2 = xF

        a = max(a1, a2)
        b = min(b1, b2)

    end_time = time.process_time()
    execution_time = end_time - start_time
    return None, max_iter, execution_time, 'hybrid_method'


file_name = "random_text_file.txt"

# فتح الملف بوضعية الكتابة (وإنشاؤه إذا لم يكن موجودًا)
# إنشاء بيانات عشوائية بحجم 10 بايت (80 بت)
random_bytes = os.urandom(10)

# تحويل البيانات العشوائية إلى نص هكساديسيمال
hex_text = random_bytes.hex()

# حفظ النص في ملف
file_name = "random.txt"
with open(file_name, 'w') as file:
    file.write(hex_text)
with open("random.txt", "rb") as file:
    plaintext_bytes = file.read()

plaintext = plaintext_bytes.decode('utf-8')  # تحويل bytes إلى string

# الآن يمكنك استخدام النص لتحويله إلى قائمة ASCII
digits = [ord(char) for char in plaintext]

# تحويل digits إلى string
plaintext = ''.join(chr(digit) for digit in digits)
plaintext_bits = len(plaintext) * 8
x_values = np.random.choice(100, len(plaintext))

print("x_values length:", len(x_values))
print("digits length:", len(digits))
degree = np.random.randint(1, 13)
if degree % 2 == 0:
    degree -= 1


def lagrange_interpolation(x, y, x_i):
    result = 0
    for i in range(len(y)):
        term = y[i]
        divisor = 1.0
        for j in range(len(x)):
            if j != i and x[i] != x[j]:  # التحقق من القسمة على الصفر
                term *= (x_i - x[j])
                divisor *= (x[i] - x[j])
        if divisor != 0:  # التحقق من عدم القسمة على الصفر
            term /= divisor
        else:
            return None  # إذا حدثت قسمة على الصفر، ارجاع قيمة None
        result += term
    return result


y_values = [lagrange_interpolation(x_values, digits, x)
            for x in x_values if lagrange_interpolation(x_values, digits, x) is not None]
poly = np.poly1d(np.polyfit(x_values, y_values, degree))
print("poly:", poly)


def generate_key():

    key = hybrid_method(poly, 0.0001, 1)

    if key is None or not isinstance(key, (int, float)):
        return os.urandom(8)  # Return 8 bytes

    return key.to_bytes(8, byteorder='big')


print(f"used_key: {generate_key}")


def encrypt_file(file_path, key, iv):
    with open(file_path, 'rb') as file:
        plaintext = file.read()
    cipher = Cipher(algorithms.TripleDES(key), modes.CFB8(iv),
                    backend=default_backend())
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(plaintext) + encryptor.finalize()

    with open(file_path + '.enc', 'wb') as encrypted_file:
        encrypted_file.write(ciphertext)


def decrypt_file(file_path, key, iv):
    with open(file_path, 'rb') as file:
        ciphertext = file.read()

    cipher = Cipher(algorithms.TripleDES(key), modes.CFB8(iv),
                    backend=default_backend())

    decryptor = cipher.decryptor()
    decrypted_text = decryptor.update(ciphertext) + decryptor.finalize()

    with open(file_path[:-4] + '_decrypted1.txt', 'wb') as decrypted_file:
        decrypted_file.write(decrypted_text)


def measure_performance(file_path, key, num_iterations=100):
    iv = os.urandom(8)  # 8 bytes for DES block size
    total_encryption_time = 0
    total_decryption_time = 0
    total_bytes_processed = 0

    for _ in range(num_iterations):
        start_time = time.time()
        encrypt_file(file_path, key, iv)
        end_time = time.time()
        total_encryption_time += (end_time - start_time)

        start_time = time.time()
        decrypt_file(file_path + '.enc', key, iv)
        end_time = time.time()
        total_decryption_time += (end_time - start_time)

        total_bytes_processed += os.path.getsize(file_path)

    average_encryption_time = total_encryption_time / num_iterations
    average_decryption_time = total_decryption_time / num_iterations
    total_processed_bytes = total_bytes_processed * num_iterations

    print(f"Avg Encryption Time: {average_encryption_time:.6f} seconds")
    print(f"Avg Decryption Time: {average_decryption_time:.6f} seconds")
    print(f"Total Bytes Processed: {total_processed_bytes} bytes")


if __name__ == "__main__":
    file_path = 'test.txt'
    key = generate_key()

    measure_performance(file_path, key)
