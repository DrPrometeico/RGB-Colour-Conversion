coloursFile = open("colours.txt", "w")
global typeName
typeName = input("What's the name of this list? ")
global numCount
numCount = 1

def converter():
    r1 = float(input("What is the R value? "))
    g1 = float(input("What is the G value? "))
    b1 = float(input("What is the B value? "))
    if (r1 > 1):
        coloursFile.close()
        exit()
    else:
        r2 = int(round((r1 * 255), 0))
        g2 = int(round((g1 * 255), 0))
        b2 = int(round((b1 * 255), 0))
        h1 = hex(r2)[2:]
        h2 = hex(g2)[2:]
        h3 = hex(b2)[2:]
        rgbFinal = ("rgb(" + str(r2) + ", " + str(g2) + ", " + str(b2) + ");")
        hexFinal = ("#" + str(h1) + str(h2) + str(h3))
        print(rgbFinal + " " + hexFinal)
        global numCount
        coloursFile.write(typeName + str(numCount) + ": " + rgbFinal + " HEX: " + hexFinal + "\n")
        numCount += 1




i = 1
while (i != 2):
    converter()

