def cript(texto1):
    texcript = ""
    i = 0
    while i < len(texto1):
            cript = ord(texto1[i])
            texcript = texcript + chr(cript + 5)
            print(texcript)
            i+=1
    print("Decrypt?")
    check = input(str())
    if (check == "y"):
        descript(texcript)
    elif (check == "n"):
        print("Closing")
    else:
        print("Invalid command")
        print("closing")



def descript(texto2):
    i = 0
    descript = ""
    while i < len(texto2):
            cript = ord(texto2[i])
            descript = descript + chr(cript - 5)
            print(descript)
            i+=1

texto1 = input()
cript(texto1)

