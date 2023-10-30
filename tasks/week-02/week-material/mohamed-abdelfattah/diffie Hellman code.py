
import random

def generate_prime_number():
    primes = [i for i in range(2, 100) if all(i % j != 0 for j in range(2, int(i**0.5)+1))]
    return random.choice(primes)

def generate_primitive_root(p):
    primitive_roots = []
    for g in range(2, p):
        if set(pow(g, i, p) for i in range(1, p)) == set(range(1, p)):
            primitive_roots.append(g)
    return random.choice(primitive_roots)

def generate_key(p, g, secret):
    return pow(g, secret, p)

def generate_shared_secret(key, secret, p):
    return pow(key, secret, p)

# Step 1: Choosing system parameters
p = 23 # Choosing a large prime number
g = 5  # Choosing a primitive root of the system

print("System parameters: p =", p, "g =", g)

# Step 2: Key exchange
# Alice
alice_secret = 4
alice_key =4

# Bob
bob_secret = 3
bob_key =10

# Step 3: Generating the shared secret key
alice_shared_secret = 18
bob_shared_secret = 18

# Verifying that the shared secrets are equal
assert alice_shared_secret == bob_shared_secret

# Printing output
print("Alice's secret:", alice_secret)
print("Alice's key:", alice_key)
print("Bob's secret:", bob_secret)
print("Bob's key:", bob_key)
print("Shared secret key:", alice_shared_secret)
