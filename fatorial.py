
def calcular_fatorial(n):
    if n < 0:
        return "Fatorial não existe para números negativos"
    elif n == 0 or n == 1:
        return 1
    else:
        fatorial = 1
        for i in range(2, n + 1):
            fatorial *= i
        return fatorial
    
numero = int(input("Digite um valor: "))
resultado = calcular_fatorial(numero)
print(f"O fatorial de {numero} é {resultado}")