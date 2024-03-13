#Zad4
# def czy_prostokatny(a, b, c):
#     if a <= 0 or b <= 0 or c <= 0:
#         return False
#
#     a, b, c = sorted([a, b, c])
#
#     return a ** 2 + b ** 2 == c ** 2
#
# a = 3
# b = 4
# c = 5
# print(czy_prostokatny(a, b, c))

#Zad5
# def pole_trapezu(a=0, b=0, h=0):
#
#     if a <= 0 or b <= 0 or h <= 0:
#         return "Błędne dane - długości boków i wysokość muszą być dodatnie."
#
#     pole = 0.5 * (a + b) * h
#     return pole
#
# print("Pole trapezu: ", pole_trapezu())

#Zad6
# def iloczyn_ciagu(a=1, b=4, ile=10):
#
#     if ile <= 0:
#         return "Błąd: Parametr 'ile' musi być liczbą dodatnią."
#
#     wynik = 1
#     for i in range(ile):
#         wynik *= a
#         a *= b
#     return wynik
#
# print("Iloczyn ciągu: ", iloczyn_ciagu())

#Zad7
# import math
# try:
#     liczba = float(input("Podaj liczbę: "))
#
#     if liczba < 0:
#         raise ValueError("Nie można obliczyć pierwiastka z liczby ujemnej.")
#
#     pierwiastek = math.sqrt(liczba)
#     print("Pierwiastek z {} wynosi: {}".format(liczba, pierwiastek))
#
# except ValueError as ve:
#     print("Błąd:", ve)
# except Exception as e:
#     print("Wystąpił nieoczekiwany błąd:", e)


