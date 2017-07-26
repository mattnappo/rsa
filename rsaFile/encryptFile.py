# -*- coding: utf-8 -*-
from rsaFile import Key, Change
import os
myKey = Key("yo")
newpath = myKey.name
if os.path.exists(newpath):
    myKey.start()
    x = Change(myKey.getPublic(), myKey.getPrivate())
    file = "target.txt"
    x.decrypt(file)
else:
    os.makedirs(newpath)
    if myKey.generate() == True:
        print("Key generation " + newpath + " successful.")