contents = "hey"
def encrypt(file):
    with open(file, "r") as r:
        print(contents)
        contents = r.read()

class Encrypter():
    def __init__(self):
        self.contents = ""
    def enc(self, file):
        with open(file, "rb") as r:
            self.contents = r.read()
            print(self.contents)
            #change to int
            #do math to int
            #go back to byte
        print(type(bytearray(self.contents)))
ec = Encrypter()
ec.enc("img.jpg")
