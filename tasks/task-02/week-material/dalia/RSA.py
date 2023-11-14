import random
import math

#check if the generated number is prime or not
def is_prime(number):
    if number < 2 :
        return False
    for i in range(2, number // 2 + 1):
        if number % i == 0:
            return False
    return True

#generate prime numbers
def generate_prime(min_val,max_val):
    prime = random.randint(min_val,max_val)
    while not is_prime(prime):
        prime = random.randint(min_val,max_val)
    return prime

#generate d for private key
def mod_inverse(e , phi_n):
    for d in range (3,phi_n):
        if (d * e) % phi_n == 1:
            return d
    raise ValueError ("mod_inverse does not exist")

# generate two prime numbers p,q
p , q = generate_prime(1000 , 10000) , generate_prime(1000 , 10000)
#check p not equal q
while p == q:
    q = generate_prime(1000 , 10000)
# calculate n 
n = p * q 
# calculate phi_n
phi_n = (p - 1) * (q - 1)
#choose e 
e = random.randint(2,phi_n -1)
#check e , phi_n are co_prime
while math.gcd(e , phi_n) != 1:
    e = random.randint(2,phi_n -1)
#find d for private key
d = mod_inverse(e , phi_n) 

print("p : " , p )
print("q : " , q )
print("n : " , n )
print("phi_n : " , phi_n ) 
print("public key (n,e) : " ,n , " , " ,e )
print("private key (n,d) : " ,n , " , " , d )

#encryption
#take the message to be encrypted from user
message = input("Enter the message to be encrypted: ")
# convert alphanumric message into numric message using ASCII code
message_encoded = [ord(ch) for ch in message]
# encode the message (c = m^e mod n )
ciphertext = [pow(ch,e,n) for ch in message_encoded]
print("Message after encryption : ", ciphertext)

#decryption
#dencrypt the encrypted message into the ASCII code of orginal message
message_encoded = [pow(ch,d,n) for ch in ciphertext] 
#convert ASCII code into the orginal message
message = "".join(chr(ch) for ch in message_encoded ) 
print("The original message is : " , message)




    