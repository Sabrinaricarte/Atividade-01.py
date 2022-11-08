quantidadePares = 0
quantidadeImpares = 0
ePar = 0
eImpar = 0
num = 0
numeros = []

for n in range (0, 6):
    numeros.append(int(input(f"Informe o {n+1} Número: ")))
print("Pares: ")
for n in range (0, 6):
    if numeros[n] % 2 == 0:
        print(numeros[n])
        ePar += 1
print("Impares: ")
for n in range (0, 6):
    if numeros[n] % 2 == 1:
        print(numeros[n])
        eImpar += 1

print(f"A quantidade de números pares: {ePar}")
print(f"A quantidade de números impares: {eImpar}")