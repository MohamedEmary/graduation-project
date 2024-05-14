byte_representation_max = "~~~~~~~~~~".encode('utf-8')
byte_representation_min = "          ".encode('utf-8')

byte_representation_max = int.from_bytes(
    byte_representation_max, byteorder='big')
byte_representation_min = int.from_bytes(
    byte_representation_min, byteorder='big')

print(byte_representation_max)
print(byte_representation_min)
