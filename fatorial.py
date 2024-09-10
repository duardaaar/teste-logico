
def calcular_fatorial(n):

    # verifica se o número é negativo

    if n < 0:
        return "Fatorial não existe para números negativos"
    
    # verifica se o número é 0 ou 1
    
    elif n == 0 or n == 1:
        return 1
    
    # inicializa a variável fatorial com 1

    else:
        fatorial = 1
        for i in range(2, n + 1):

            # multiplica o valor atual de fatorial pelo valor de i
            
            fatorial *= i
        return fatorial
    
numero = int(input("Digite um valor: "))
resultado = calcular_fatorial(numero)
print(f"O fatorial de {numero} é {resultado}")