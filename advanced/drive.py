# -*- coding: utf-8 -*-
from rsa import Key, Modifier
import os
inp = input("E or D? ")
def looper(directory):
    files = os.listdir(directory)
    for x in range(len(files)):
        file = files[x]
        if os.path.isdir(directory + "/" + file) == True:
            print(file + " is a dir")
            looper(directory + "/" + file)
        else:
            if inp == "E":
                modifier.encrypt(directory + "/" + file)
                print(file + " encrypted")
            elif inp == "D":
                modifier.decrypt(directory + "/" + file)
                print(file + " decrypted")

myKey = Key("basicKey")
newpath = myKey.name
if os.path.exists(myKey.name):
    myKey.start()
    modifier = Modifier(myKey.getPublic(), myKey.getPrivate())
    looper("./encryptme")
else:
    os.makedirs(newpath)
    if myKey.generate() == True:
        print("Key generation " + newpath + " successful.")
