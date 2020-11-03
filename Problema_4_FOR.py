a, b = input("Dati numerele a si b (separate prin spatiu): ").split()
a = int(a)
b = int(b)
if a < b:
    for n in range(a, b):
        if (n % 2 != 0):
            print(n)