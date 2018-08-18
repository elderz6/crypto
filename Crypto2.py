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
        decript(texcript)
    elif (check == "n"):
        print("Closing")
    else:
        print("Invalid command")
        print("closing")



def decript(texto2):
    i = 0
    decript = ""
    while i < len(texto2):
            cript = ord(texto2[i])
            decript = decript + chr(cript - 5)
            print(decript)
            i+=1

texto1 = input()
cript(texto1)

