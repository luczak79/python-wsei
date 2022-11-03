#Kalkulator
import os
from decimal import Decimal


def menuKalkulator():
    print("----==== Kalkulator ====----")
    print("[1] - Dodawanie")
    print("[2] - Odejmowanie")
    print("[3] - Dzielenie")
    print("[4] - Mnożenie")
    print("[5] - Potęgowanie")
    print("[6] - Zakończ działanie programu")

def pobierzRodzajDzialania():
    dzialanie = 0;
    while dzialanie not in ['1','2','3','4','5','6']:
        dzialanie = input("Jakie działanie chesz wykonać? Podaj liczbę od 1 do 6: ")
    return dzialanie

def dodawanie(skladnik1, skladnik2):
    return skladnik1 + skladnik2

def odejmowanie(odjemna, odjemnik):
    return odjemna - odjemnik

def dzielenie(dzielna, dzielnik):
    if (dzielnik == 0):
        return "BLAD"
    else:
        return dzielna / dzielnik

def mnozenie(czynnik1, czynnik2):
    return czynnik1 * czynnik2

def potegowanie(podstawa, wykladnik):
    if (wykladnik == 0):
        return 1
    if (wykladnik < 0):
        return (1/podstawa)**(-wykladnik)
    return podstawa ** wykladnik

def pobieranieLiczby(tekst):
    while True:
        liczba1 = input(tekst)
        liczba1 = float(liczba1)
        if isinstance(liczba1, float):
            return liczba1

def wykonajDzialanie(dzialanie, liczba1, liczba2):
    if (dzialanie == '1'):
        print('Dodawanie: {0}+{1}'.format(liczba1, liczba2) )
        return tablicaWynikow.append(str(dodawanie(liczba1, liczba2)))
    elif (dzialanie == '2'):
        print('Odejmowanie: {0}-{1}'.format(liczba1, liczba2))
        return tablicaWynikow.append(str(odejmowanie(liczba1, liczba2)))
    elif (dzialanie == '3'):
        print('Mnożenie: {0}*{1}'.format(liczba1, liczba2))
        return tablicaWynikow.append(str(mnozenie(liczba1, liczba2)))
    elif (dzialanie == '4'):
        print('Dzielenie: {0}/{1}'.format(liczba1, liczba2))
        return tablicaWynikow.append(str(dzielenie(liczba1, liczba1)))
    elif (dzialanie == '5'):
        print('Potegowanie: {0}**{1}'.format(liczba1, liczba2))
        return tablicaWynikow.append(str(potegowanie(liczba1, liczba2)))
    else:
        return "Błąd w obliczeniach!!!"


tablicaWynikow = []
operacja = '0'
while operacja != '6':
    menuKalkulator()
    operacja = pobierzRodzajDzialania()
    if (operacja == '6'):
        tablicaWynikow.append("")
        break
    else:
        liczba1 = pobieranieLiczby("Pobranie pierwszej liczby: ")
        liczba2 = pobieranieLiczby("Pobranie drugiej liczby: ")
        wykonajDzialanie(operacja, liczba1, liczba2)
print("Wynik działań: ", ' '.join(tablicaWynikow))


