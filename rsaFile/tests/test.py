def intToBytes(i):
    if i == 0:
        return b""
    else:
        return intToBytes(i//256) + bytes([i%256])

num = 12341234
print(intToBytes(num))
print(int.from_bytes(intToBytes(num), byteorder="big"))
print(num.to_bytes(8, byteorder="big"))
