class Encrypter():
    def __init__(self):
        self.contents = None
    def intToBytes(self, i):
        if i == 0:
            return b""
        else:
            return self.intToBytes(i//256) + bytes([i%256])
    def enc(self, file):
        with open(file, "rb") as r:
            self.contents = bytearray(r.read())
        with open(file, "wb") as w:
            encr = 0
            for byte in range(len(self.contents)):
                encr = self.contents[byte]**self.public[0]%self.public[1]
                w.write(self.intToBytes(encr))

ec = Encrypter()
ec.enc("img.jpg")
