import base64 as base

while 1:
    var01 = str(input("Do you want to encode or decode? (e/d): "))

    if var01 == 'e' or var01 == 'E':
        print("Type the message you want to encode (It'll be utf-8)")
        var1 = str(input("> "))
        var2 = bytes(var1, "utf-8")
        print("Encoded message: ", base.b64encode(var2))
    
    elif var01 == 'd' or var01 == 'D':
        print("Type the message you want to decode (it must be utf-8)")
        var1 = str(input("> "))
        var2 = bytes(var1, "utf-8")
        print("Decoded message: ", base.b64decode(var2))
    
    else:
        print("...")
    
    var4 = str(input("Do you want to continue using this program? (y/n)"))

    if var4 == 'y' or var4 == 'Y':
        print("Alright")
    
    elif var4 == 'n' or var4 == 'N':
        print("Alright")
        break

    else:
        print("...")

