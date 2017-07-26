val = input("Enter a string: ")
new = []
def show():
    for x in range(len(new)):
        print(new[x], end="")
    print()
def slide(encr):
    for x in range(len(val)):
        number = ord(val[x])
        new.append(chr(number+encr))
    show()
slide(3)