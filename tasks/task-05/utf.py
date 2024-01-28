def textToIntUTF(text):
    # Convert the text to bytes using UTF-8 encoding
    byte_representation = text.encode('utf-8')
    # Convert the bytes to integer
    integer_representation = int.from_bytes(
        byte_representation, byteorder='big')
    return integer_representation


def normalize(num):
    min = 35322350018592
    max = 139081753198206
    return (num - min)/(max-min)


def denormalize(num):
    min = 35322350018592
    max = 139081753198206
    return num*(max-min) + min


def intToTextUTF(num):
    # Convert the integer to bytes using UTF-8 encoding
    byte_representation = num.to_bytes(
        (num.bit_length() + 7) // 8, byteorder='big')
    # Convert the bytes to string using UTF-8 encoding
    text = byte_representation.decode('utf-8')
    return text


print(textToIntUTF('~~~~~~'))  # 139081753198206
print(textToIntUTF('      '))  # 35322350018592

text = "odha#@"
print(normalize(textToIntUTF(text)))
res = normalize(textToIntUTF(text))
print(textToIntUTF(text))

res = denormalize(res)

print(intToTextUTF(int(res)))

# 2
# 1.999999
# Higher Precision Means more iterations with root finding algorithm
