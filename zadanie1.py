tekst1 = "Marcin"
tekst2 = "Łuczak"
liczba = 5

# pierwsza_zmienna * druga_zmienna
# wynik1 = tekst1 * tekst2
# print(wynik1)
# Traceback (most recent call last):
#   File "C:\Users\lucza\PycharmProjects\lab_30_10_2022\zadanie1.py", line 6, in <module>
#     wynik1 = tekst1 * tekst2
# TypeError: can't multiply sequence by non-int of type 'str'
# Nie możemy wykonać takiego działania

# pierwsza_zmienna + druga_zmienna
wynik1 = tekst1 + tekst2
print(wynik1)
# Wynik działania: MarcinŁuczak

# pierwsza_zmienna * trzecia_zmienna
print(tekst1 * liczba)
# Wynik działania: MarcinMarcinMarcinMarcinMarcin

# pierwsza_zmienna + trzecia_zmienna
# print(tekst1 + liczba)
# Traceback (most recent call last):
#   File "C:\Users\lucza\PycharmProjects\lab_30_10_2022\zadanie1.py", line 24, in <module>
#     print(tekst1 + liczba)
# TypeError: can only concatenate str (not "int") to str
# Próba napraway:
print(tekst1 + str(liczba))
# Wynik: Marcin5

