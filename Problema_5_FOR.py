n = int(input("Dati un numar: "))
suma = 0
for num in range(1, n):
    if (num % 3 == 0) and (num % 5 == 0):
        suma += num
print(suma)