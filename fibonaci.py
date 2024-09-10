def fibonacci(n):
    # verifica se o número é válido
    if n <= 0:
        return "O número deve ser maior que zero."
    elif n == 1:
        return [0]
    
    # inicializando a sequência com os dois primeiros números
    sequencia = [0, 1]
    
    # gerando a sequência até o n-ésimo número
    for i in range(2, n):
        proximo = sequencia[-1] + sequencia[-2]  # soma dos dois últimos números
        sequencia.append(proximo)
    
    return sequencia

n = int(input("Digite o número de termos da sequência de Fibonacci que deseja: "))
resultado = fibonacci(n)
print(f"A sequência de Fibonacci até o {n}-ésimo número é: {resultado}")