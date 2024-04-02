# #Zad1
# #a)
# import math
# a = (math.exp(4) - math.log(34, 2)) ** (1/3)
#
# wynik1 = round(a,2)
#
# print("Wartość wyrażenia a wynosi:", wynik1)
#
# #b)
# b = (math.log(20) + math.cos(math.radians(45)) + math.exp(1)) ** (1/3)
#
# wynik2 = round(b,2)
#
# print("Wartość wyrażenia b wynosi:", wynik2)
#
# #c)
# c = (math.log(20, 3) + math.sin(math.radians(45)) * (5/8)) ** (1/4)
#
# wynik3 = round(c,2)
#
# print("Wartość wyrażenia c wynosi:", wynik3)
#
# #d)
# d = math.log(23, 3) + (math.sin(math.radians(34)) + 5) ** (1/3)
#
# wynik4 = round(d,2)
#
# print("Wartość wyrażenia d wynosi:", wynik4)
#
# #e)
# e = (math.log(32, 2) + math.pi + math.sin(math.radians(56))) ** (1/4)
#
# wynik5 = round(e,2)
#
# print("Wartość wyrażenia e wynosi:", wynik5)


# #Zad2
# def rysuj_wieżę(wysokosć):
#     if wysokość > 10:
#         print("Wysokość wieży nie może być większa niż 10.")
#         return
#
#     for i in range(1, wysokość + 1):
#         print("A" * i)
#
# wysokość = int(input("Podaj wysokość wieży (maksymalnie 10): "))
# rysuj_wieżę(wysokość)

# #Zad3
# def rysuj_piramidę(wysokość):
#     if wysokość > 10:
#         print("Wysokość piramidy nie może być większa niż 10.")
#         return
#
#     for i in range(1, wysokość + 1):
#         print(" " * (wysokość - i), end="")
#         print("A" * (2 * i - 1))
#
# wysokość = int(input("Podaj wysokość piramidy (maksymalnie 10): "))
# rysuj_piramidę(wysokość)

#Zad4


#Zad5
import random
def suma_wierszy_macierzy(n):
    macierz = [[random.randint(1, 10) for _ in range(n)] for _ in range(n)]
    suma_wierszy = [sum(wiersz) for wiersz in macierz]

    return suma_wierszy

n = int(input("Podaj wymiar macierzy (n): "))
suma_wierszy = suma_wierszy_macierzy(n)
print("Suma każdego wiersza macierzy:", suma_wierszy)