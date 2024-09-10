def verifica_aprovacao(n1, n2):

    media = (n1 + n2) / 2

    if media >= 7:
        return "Aluno(a) aprovado!!! :)"
    elif media < 5:
        return "Aluno(a) nao atingiu a média. Reprovado! :("
    else:
        return "resposta inválida"


n1 = float(input("Insira a primeira nota: "))
n2 = float(input("Insira a segunda nota: "))
resultado = verifica_aprovacao(n1, n2)
print(resultado)
    