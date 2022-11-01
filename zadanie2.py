# Zadanie 2
# Proszę zapoznać się z dokumentacją klasy string, a następnie sprawdzić działanie funkcji rjust(),
# strip(), isnumeric() na wybranych przykładach.

#rjust()
tekst = "Marcin"
x = tekst.rjust(40)
print(x, " Łuczak")
#Wynik:                                   Marcin  Łuczak
#lub
y = tekst.rjust(40, "-")
print(y, " Łuczak")
#Wynik: ----------------------------------Marcin  Łuczak

#strip()
imie = "    Marcin Łuczak   "
print("Imie: ", imie)
print("Imie: ", imie.strip())
# Wynik
# Imie:      Marcin Łuczak
# Imie:  Marcin Łuczak

#isnumeric()
test1 = "Marcin"
test2 = "5"
test3= "6.4"
test4 = "7,1"
testy = [test1, test2, test3, test4]

for test in testy:
    print(test.isnumeric())

#Wynik:
# False
# True
# False
# False

