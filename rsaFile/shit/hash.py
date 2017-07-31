import hashlib

with open("password.txt", "w") as file:
    file.write(hashlib.sha512("hey".encode("utf-8")).hexdigest())
    
user = input("Enter a password: ")

with open("password.txt", "r") as file:
    if hashlib.sha512(user.encode("utf-8")).hexdigest() == file.read():
        print("YAA")
    else:
        print("NAHH")