# 1 byte = 8 bits
# 10011011 = 8 bits = 1 byte
# 10110110 01100011 000001100 = 3 * 8 bits = 3 bytes

# We can take the first 6 bits
# 101101 100110 001100 001100 = 4 * 6 bits

# Why do we care?
# Base64 encodes Binary Data => text data

# Mailing protocol = Transmission of TEXT != Image/Binary Data
import base64

my_text = 'Hello World'
# Encoding my_text to ascii
my_text = my_text.encode()
my_text_b64 = base64.b64encode(my_text)
print(f'my_text_b64')
print(my_text_b64)

# When someone takes it
# They can just decode it
my_text_b64decode = base64.b64decode(my_text_b64)
print(my_text_b64decode.decode())
#print(my_text_b64decode.decode("ascii"))
