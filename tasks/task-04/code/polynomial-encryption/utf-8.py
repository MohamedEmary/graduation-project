import random
import string


def generate_random_text(bits=80):
    # calculate the number of characters needed to represent 80 bits
    chars = bits // 8
    # generate a random string of alphanumeric characters
    text = "".join(random.choice(string.ascii_letters + string.digits)
                   for _ in range(chars))
    # return the text
    return text


def convert_to_decimal_and_hexa(text):
    # encode the text as a bytes object using utf-8
    bytes = text.encode("utf-8")
    # convert the bytes object to an integer using int.from_bytes
    decimal_num = int.from_bytes(bytes, "big")
    hexa_num = hex(decimal_num)
    # return the number
    return decimal_num, hexa_num


def convert_to_text(number):
    # convert the number to a bytes object using int.to_bytes
    bytes = number.to_bytes((number.bit_length() + 7) // 8, "big")
    # decode the bytes object using utf-8
    text = bytes.decode("utf-8")
    # return the text
    return text


# test the function
random_text = generate_random_text()
print(random_text)
decimal_num, hexa_num = convert_to_decimal_and_hexa(random_text)
print(hexa_num)
print(decimal_num)
string = convert_to_text(decimal_num)
print(string)
