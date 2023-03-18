def zad1():
    text = " Python 2023"
    a = id(text)
    b = id(text)
    c = id(text)

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
def zad2():
    a = int(input())
    c = input()
    b = int(input())
    print("=")

    match c:
        case "+":
            print(a + b)
        case "-":
            print(a - b)
        case "*":
            print(a * b)
        case "/":
            print(a / b)
        case _:
            print("Błąd - zły operator")
def zad3():
    print("Jak masz na imię oraz nazwisko?")
    odp1 = input()

    print("Najczęstszym sposobem spędzania wolnego czasu jest dla Ciebie:")
    answers1 = ["oglądanie telewizji/filmów/seriali", "Czytanie książek/czasopism", "słuchanie muzyki",
                "spotkanie z rodziną/przyjaciułmi", "podróżowanie", "uprawianie sportu", "inne"]
    i=1
    for line in answers1:
        print(str(i)+" - " +line)
        i+=1
    odp2 = answer(input(), answers1)

    print("W jakich okolicznościach czytasz najczęściej?")
    answers2 = ["podczas podróży", "w czasie wolnym(po pracy, na urlopie)", "podczas pracy/nauki (to ich element)",
                "w pgóle nie czytam", "inne"]
    i = 1
    for line in answers2:
        print(str(i) + " - " + line)
        i += 1
    odp3 = answer(input(), answers2)

    print()
    print("Pytanie: " + "Jak masz na imię oraz nazwisko?")
    print("Odpowiedź: " + odp1)
    print("Pytanie: " + "Najczęstszym sposobem spędzania wolnego czasu jest dla Ciebie:")
    print("Odpowiedź: " + odp2)
    print("Pytanie: " + "W jakich okolicznościach czytasz najczęściej?")
    print("Odpowiedź: " + odp3)
def answer(number, answers):
    if number.isdigit():
        if int(number)==len(answers):
            print("Jakie?")
            return input()
        if len(answers) > int(number) > 0:
            return answers[int(number)-1]
    return "Błędna odpowiedź"


if __name__ == '__main__':
    zad1()
    zad2()
    zad3()