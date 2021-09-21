from fracao import fracaoOrdinaria

def adicao(m1, m2):
    '''Adiciona diretamente cada elemento de lista a outra.'''
    soma = []
    for i in range(len(m1)):
        soma.append(m1[i] + m2[i])
    return soma

def produtoEscalar(linha, escalar):
    '''Multiplica todos os elementos de uma lista por um número real.'''
    return [col * escalar for col in linha]
    
def elementosNulos(linha):
    '''Verifica quantos elementos nulos se tem em uma matriz linha antes do primeiro valor não-nulo.'''
    qnt = 0
    for i in linha:
        if i == 0: qnt += 1
        else: break
    return qnt

def separarEmConjuntos(matriz):
    '''Divide as linhas de uma matriz em listas conforme a quantidade de zeros antes de elementos não-nulos.'''
    conjuntos = [[] for i in range(len(matriz[0])+1)] # gera matriz de mesmo tamanho das linhas
    for linha in matriz:
        pos = elementosNulos(linha)
        conjuntos[pos] += [linha]
    return conjuntos

def escalonar(matriz):
    '''Escalona matriz se operando entre linhas.'''
    separados = separarEmConjuntos(matriz) # separa em listas
    for conjunto in separados:
        # se a lista possuir mais de um elemento, então há o que se escalonar
        if len(conjunto) > 1: 
            pos = elementosNulos(conjunto[0])
            # cálculo do coeficiente para o anulamento de termo
            coef = -conjunto[-1][pos]/conjunto[0][pos] 
            # apaga o elemento anulado da matriz
            del matriz[matriz.index(conjunto[-1])]
            # calcula o novo termo com base no coeficiente encontrado
            novoTermo = adicao(conjunto[-1], produtoEscalar(conjunto[0], coef))
            # adiciona à matriz
            matriz.append(novoTermo)
            # exibe qual operação entre linhas foi feita
            coefStr = str(fracaoOrdinaria(coef))
            print(f"L{len(conjunto)} = L{len(conjunto)}{'+'+coefStr if coef >= 0 else coefStr}*L1")
            # repete o processo
            return escalonar(matriz)
    # se não houver mais o que se escalonar, se retorna a matriz escalonada
    return matriz

def exibir(matriz):
    '''Exibe uma matriz se dividindo em linhas e se pondo o necessário em frações ordinárias.'''
    for linha in matriz:
        print('[', end=" ")
        for col in linha: print(fracaoOrdinaria(col), end=" ")
        print(']')