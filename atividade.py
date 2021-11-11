import math
n = int(input("Digite um numero inteiro"))
print ("Numero sucessor: ", n + 1)
print ("Numero antecessor: ", n - 1)
print ("Dobro do numero: ", n * 2)
print ("Numero ao cubo: ", n ** 3)
print ("Numero em sua raiz quadrada: ", math.sqrt(n))

print ("Tabuada do numero: ", n)
aux = 1
while aux <= 10:
    print (n, "X", aux, "=", n * aux)
    aux = aux + 1
