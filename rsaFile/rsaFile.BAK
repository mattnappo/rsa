# -*- coding: utf-8 -*-
import fractions, random, os, io, struct
class Key():
    def __init__(self, name):
        self.name = name
        self.public = []
        self.private = []
    def start(self):
        files = [self.name + "/" + self.name + "_n.rsa", self.name + "/" + self.name + "_public.rsa", self.name + "/" + self.name + "_private.rsa"]
        with open(files[0], "r") as nVal:
            with open(files[1], "r") as e:
                nv = int(nVal.read())
                self.public = [int(e.read()), nv]
            with open(files[2], "r") as d:
                self.private = [int(d.read()), nv]
    def generate(self):
        self.public = []
        self.private = []
        self.p = 61 # one prime
        self.q = 53 # another prime
        self.n = (self.p)*(self.q) # the modulo
        self.totient = (self.p-1)*(self.q-1) # totient
        self.e = 2
        while True:
            if fractions.gcd(self.e, self.totient)==1: # if coprime
                break
            else:
                self.e = random.randint(2, self.totient) # continue to pick a random number in the range 1 < e < totient
        self.d = 2
        while True:
            if (self.d)*(self.e)%self.totient==1: # if modulo of de == 1
                break
            else:
                self.d = random.randint(2, self.n)
        self.public = [self.e, self.n]
        self.private = [self.d, self.n]
        files = [self.name + "/" + self.name + "_n.rsa", self.name + "/" + self.name + "_public.rsa", self.name + "/" + self.name + "_private.rsa"]
        values = [self.n, self.e, self.d]
        for x in range(len(files)):
            with open(files[x], "w") as xFile:
                xFile.write(str(values[x]))
        return True
    def getPublic(self):
        return self.public
    def getPrivate(self):
        return self.private
class Change():
    def __init__(self, public, private):
        self.public = public
        self.private = private
        self.contents = ""
    def intToBytes(self, i):
        if i == 0:
            return b""
        else:
            return self.intToBytes(i//256) + bytes([i%256])
    def encrypt(self, file):
        with open(file, "rb") as r:
            self.contents = bytearray(r.read())
        open(file, "wb").close()
        with open(file, "wb") as w:
            encr = 0
            for x in range(len(self.contents)):
                encr = self.contents[x]**self.public[0]%self.public[1]
                print(encr)
                w.write(self.intToBytes(encr))
    def decrypt(self, file):
        with open(file, "rb") as r:
            self.contents = bytearray(r.read())
        open(file, "wb").close()
        with open(file, "wb") as w:
            encr = 0
            for byte in range(len(self.contents)):
                encr = self.contents[byte]**self.private[0]%self.private[1]
                w.write(self.intToBytes(encr))
