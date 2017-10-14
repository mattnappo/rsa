# -*- coding: utf-8 -*-
from rsa import Key, Modifier
import os
inp = input("E or D? ").lower()
def looper(directory):
    files = os.listdir(directory)
    for x in range(len(files)):
        file = files[x]
        if os.path.isdir(directory + "/" + file) == True:
            print(file + " is a dir")
            looper(directory + "/" + file)
        else:
            if inp == "e":
                modifier.encrypt(directory + "/" + file)
                print(file + " encrypted")
            elif inp == "d":
                modifier.decrypt(directory + "/" + file)
                print(file + " decrypted")

myKey = Key("basicKey")
new = myKey.name
if os.path.isfile(new + ".json"):
    myKey.start()
    modifier = Modifier(myKey.getPublic(), myKey.getPrivate())
    looper("./encryptme")
else:
    if myKey.generate() == True:
        print("Key generation " + new + " successful.")
