import sys

# Zadanie 3
# Proszę sprawdzić funkcjonalność metody maxsize z biblioteki sys i opisać jej działanie w komentarzu.

# Metoda zwraca maksymalny rozmiar list i stringów w pythonie. Wartość zależna jest od platformy.
print(sys.maxsize)

#Stworzenie listy o maksymalnym rozmiarze
list = range(sys.maxsize)
print(len(list))

#Wynik działania
# 9223372036854775807
# 9223372036854775807

# Utworznie listy przekraczajacej rozmiar maxsize
list = range(sys.maxsize + 1)
print(len(list))
# Traceback (most recent call last):
#   File "C:\Users\lucza\PycharmProjects\lab_30_10_2022\zadanie3.py", line 18, in <module>
#     print(len(list))
# OverflowError: Python int too large to convert to C ssize_t

