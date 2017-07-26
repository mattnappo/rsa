with open("testfile","r") as xFile:
    contents = xFile.read()

print(bytearray(contents, "utf-8"))
print(type(bytearray(contents, "utf-8")))

with open("testfile", "wb") as xFile:
    xFile.write(bytearray("hi", "utf-8"))