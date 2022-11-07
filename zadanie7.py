def pobierzDaneTrojkata(): 
    bokiTrojkata = []
    for i in range(3):
        info = "Podaj długość boku nr " + str(i+1) + ":"
        bok = input(info)
        bok = int(bok)
        bokiTrojkata.append(bok)
    return bokiTrojkata

def testTrojkat(boki):
    a = boki[0]
    b = boki[1]
    c = boki[2]
    isTrojkat = (b + c > a) or (c + a > b) or (a + b > c)
    if isTrojkat:
        print("Z tych odcinków można zbudować trójkąt.")
        isProstkatny = (a*a + b*b ==c*c) or (a*a + c*c == b*b) or (c*c + b*b == a*a)

        if isProstkatny:
            print("To będzie trójkąt prostokątny.")
        else:
            print("To nie będzie trójkąt prostokątny.")        
    else:
        print("Z tych odcinków nie można zbudować trójkąta")


boki = pobierzDaneTrojkata()
print("Boki trójkąta: ", boki)
testTrojkat(boki)