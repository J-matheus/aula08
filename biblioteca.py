#exercicio01
def imprime_nome(nome):
    print(f"Nome: {nome}")

#exercicio02
def piramide(num):
    for x in range(1, num +1, 1):
        for y in range (0,x):
            print(x, end=" ")
        print()

#exercicio03
def texto(letra):
    contador = 0
    for x in letra.lower():
        if x in "aeiou":
            contador += 1
    print(contador)

#exercicio04
def loja(produto, quantidade, valorProduto):
    valorTotal=quantidade*valorProduto
    return valorTotal

#exercicio05
def necessite():
    aula = int(input("Informe um numero:"))
    if aula < 0 :
        return "N"
    if aula > 0:
        return "P"
    else:
        return "Z"

#exercicio06
def somar(a,b):
    soma = a + b
    print(soma)

#exercicio07
def calculo(*a):
    soma=0
    for s in a:
        soma +=s
    print(soma)

#exercicio08
def contrario(texto):
    contador= 0
    for i in range (len(texto.lower()) -1, -1, -1):
        if texto[i]!= " ":
            contador+=1
        print(texto[i], end=" ")
        print(i)

#exercicio09
def listagem(lista):
    novaLista=[]
    for x in lista:
        if x not in novaLista:
            novaLista.append(x)
    print(novaLista)
