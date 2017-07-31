from rsa import Key, Change
import os
myKey = Key("basicKey")
newpath = myKey.name
if os.path.exists(myKey.name):
    myKey.start()
    modifier = Change(myKey.getPublic(), myKey.getPrivate())
    modifier.encrypt("file")
else:
    os.makedirs(newpath)
    if myKey.generate() == True:
        print("Key generation " + newpath + " successful.")
