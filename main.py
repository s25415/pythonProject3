if __name__ == '__main__':

    text = " Python 2023"
    a = id(text)
    b = id(text)
    c = id(text)

    print(a==b)
    print(b==c)

    print("Type a = "+str(type(a)))
    print("Adress a = "+str(hex(a)))
    print()
    print("Type b = " + str(type(b)))
    print("Adress b = " + str(hex(b)))
    print()
    print("Type c = " + str(type(c)))
    print("Adress c = " + str(hex(c)))
    print()

    c = id("Java 11")

    print(a == b)
    print(b == c)

    print("Type a = " + str(type(a)))
    print("Adress a = " + str(hex(a)))
    print()
    print("Type b = " + str(type(b)))
    print("Adress b = " + str(hex(b)))
    print()
    print("Type c = " + str(type(c)))
    print("Adress c = " + str(hex(c)))
    print()