def organizarListaDoGrafo(lista: list) -> None:
    """
    Recebe uma lista de listas e organiza a lista colocando todos os elementos
    iguais ao elemento da lista[i][0] no início da lista[i]. Em seguida, ordena
    os elementos restantes e os coloca no fim da lista.
    """
    for i in range(len(lista)):
        vertice = lista[i][0]
        cont = 1
        for j in range(1, len(lista[i])):
            if lista[i][j] == vertice:
                cont += 1
        for k in lista[i].copy():
            if k == vertice:
                lista[i].remove(k)
        lista[i].sort()
        for l in range(cont):
            lista[i].insert(0, vertice)
    lista.sort()

def criarListaDaGrau(lista: list) -> list:
    """
    Recebe uma lista de listas e retorna uma lista ordenada de forma decrescente
    pela quantidade de vértices que chegam apartir do vértice lista[i][1]. Caso
    haja vértices com a mesma quantidade, será ordenada de forma crescente em
    ordem alfabética pelo vértice lista[i][1].
    """
    # Lista que conterá o grau de saída de cada vértice.
    listaDeGraus = []
    # Percorro a lista e adiciono à listaDeGraus listas nesse formato: [Grau do vértice, Vértice].
    for i in range(len(lista)):
        listaDeGraus.append([len(lista[i]) - 1, lista[i][0]])
    # Ordeno a lista de ordem decrescente.
    listaDeGraus.sort(reverse=True)
    # Lista que conterá a listaDeGraus ordenada por vértices de ordem decrescente, seguido de uma ordenação
    # alfabética pelo caractér do vértice.
    novaListaDaGrau = []
    # Lista auxiliar.
    listaAuxiliarDeGraus = []
    # Ordeno também por ordem alfabética do nome do vértice.
    for i in range(len(listaDeGraus)):

        if(listaDeGraus[i][0] not in listaAuxiliarDeGraus):
            listaAuxiliarDeGraus.append(listaDeGraus[i][0])

            listaAuxiliarDeVertices = []
            cont = 0

            for j in range(len(listaDeGraus)):
                if (listaDeGraus[j][0] == listaAuxiliarDeGraus[-1]):
                    listaAuxiliarDeVertices.append(listaDeGraus[j][1])
                    cont += 1
                else:
                    j = len(listaDeGraus)

            listaAuxiliarDeVertices.sort()

            for k in range(cont):
                novaListaDaGrau.append(
                    [listaAuxiliarDeGraus[-1], listaAuxiliarDeVertices[k]])

    return novaListaDaGrau

def carregarArquivo(arquivo: str) -> list:
    """
    Recebe uma string contendo o caminho do diretório de um arquivo, caso
    o grafo seja direcionado, armazena as aresta do arquivo em uma lista e
    retorna essa lista.
    """
    arquivoAberto = open(arquivo, 'r')
    Entrada = arquivoAberto.readlines()

    # Lista que conterá listas com os vértices de cada vértice.
    verticesDeCadaVertice = []
    # Lista que conterá os vértices com chegada.
    verticesComChegada = []

    # Caso for um grafo direcionado, faz os procedimentos.
    if Entrada[0].split()[2] == "D":
        for i in range(len(Entrada)):
            linha = Entrada[i].split()
            # Caso não seja a primeira linha do arquivo, começo a preencher a as listas.
            if i > 0:
                # Verifico se o vértice linha[1] está na verticesComChegada, caso não esteja, adiciono-o.
                if linha[1] not in verticesComChegada:
                    verticesComChegada.append(linha[1])
                # Verifico se a lista do vértice linha[0] já está na lista verticesDeCadaVertice. Caso esteja, defino qual o índice dessa lista na lista verticesDeCadaVertice.
                estaNaLista = False
                for i in range(len(verticesDeCadaVertice)):
                    if verticesDeCadaVertice[i][0] == linha[0]:
                        estaNaLista = True
                        indiceDaListaDoVerticeLinha0 = i
                # Caso a lista do vértice linha[0] não esteja na lista verticesDeCadaVertice, é criado essa lista com o vértice linha[0] dentro dela e definimos
                # qual o indice da lista do vértice linha[0].
                if not estaNaLista:
                    verticesDeCadaVertice.append([linha[0]])
                    indiceDaListaDoVerticeLinha0 = verticesDeCadaVertice.index([
                        linha[0]])
                # Adiciono à lista do vértice linha[0] o vértice linha[1], indicando que há a aresta de linha[0] para linha[1].
                verticesDeCadaVertice[indiceDaListaDoVerticeLinha0].append(
                    linha[1])

        # Caso algum vértice de chegada não saia para nenhum outro vértice, adiciono a lista do vértice na verticesDeCadaVertice com apenas o próprio vértice.
        for i in verticesComChegada:
            cont = 0
            for j in verticesDeCadaVertice:
                if i == j[0]:
                    cont += 1
            if cont == 0:
                verticesDeCadaVertice.append([i])

        arquivoAberto.close()
        organizarListaDoGrafo(verticesDeCadaVertice)
        return verticesDeCadaVertice

    arquivoAberto.close()
    return []

def DFS(lista: list) -> None:
    global mark, cor, d, f, listaDeTipoDasArestas, verticesEmOrdemCrescente, verticesEmOrdemDeGrau

    cor = ["Branco"] * len(lista)
    d = [0] * len(lista)
    f = [0] * len(lista)

    mark = 0

    verticesEmOrdemCrescente = []
    for i in listaDeAdjacencia:
        verticesEmOrdemCrescente.append(i[0])

    verticesEmOrdemDeGrau = []
    for i in lista:
        verticesEmOrdemDeGrau.append(i[1])

    listaDeTipoDasArestas = [[], [], [], []]

    for u in range(len(lista)):
        if cor[u] == "Branco":
            DFS_VISIT(lista[u][1])

    imprimirNomeclatura(listaDeTipoDasArestas)

def DFS_VISIT(u: str) -> None:
    global mark, cor, d, f, listaDeTipoDasArestas, verticesEmOrdemCrescente, verticesEmOrdemDeGrau

    cor[verticesEmOrdemDeGrau.index(str(u))] = "Cinza"
    mark += 1
    d[verticesEmOrdemDeGrau.index(str(u))] = mark

    for v in range(len(listaDeAdjacencia[verticesEmOrdemCrescente.index(str(u))])):
        # Se o vértice for branco, ele será uma Árvore.
        if cor[verticesEmOrdemDeGrau.index(listaDeAdjacencia[verticesEmOrdemCrescente.index(str(u))][v])] == "Branco":
            listaDeTipoDasArestas[0].append(
                [str(u), str(listaDeAdjacencia[verticesEmOrdemCrescente.index(str(u))][v])])
            DFS_VISIT(
                str(listaDeAdjacencia[verticesEmOrdemCrescente.index(str(u))][v]))
        # Se o vértice for cinza, ele será um Retorno.
        elif cor[verticesEmOrdemDeGrau.index(listaDeAdjacencia[verticesEmOrdemCrescente.index(str(u))][v])] == "Cinza":
            if str(u) != str(listaDeAdjacencia[verticesEmOrdemCrescente.index(str(u))][v]):
                listaDeTipoDasArestas[1].append(
                    [str(u), str(listaDeAdjacencia[verticesEmOrdemCrescente.index(str(u))][v])])
        else:
            # Se o vértice for preto e o tempo de descoberta de u for menor que o tempo de descoberta de v, será um Avanço.
            if d[verticesEmOrdemDeGrau.index(str(u))] < d[verticesEmOrdemDeGrau.index(str(listaDeAdjacencia[verticesEmOrdemCrescente.index(str(u))][v]))]:
                listaDeTipoDasArestas[2].append(
                    [str(u), str(listaDeAdjacencia[verticesEmOrdemCrescente.index(str(u))][v])])
            # Se o vértice for preto e o tempo de descoberta de u não for menor que o tempo de descoberta de v, será um Cruzamento.
            else:
                listaDeTipoDasArestas[3].append(
                    [str(u), str(listaDeAdjacencia[verticesEmOrdemCrescente.index(str(u))][v])])

    cor[verticesEmOrdemDeGrau.index(str(u))] = "Preto"
    mark += 1
    f[verticesEmOrdemDeGrau.index(str(u))] = mark

def imprimirNomeclatura(lista: list) -> None:
    for i in range(len(lista[0])):
        print(f"{lista[0][i][0]} -> {lista[0][i][1]} (Árvore)")
    for i in range(len(lista[1])):
        print(f"{lista[1][i][0]} -> {lista[1][i][1]} (Retorno)")
    for i in range(len(lista[2])):
        print(f"{lista[2][i][0]} -> {lista[2][i][1]} (Avanço)")
    for i in range(len(lista[3])):
        print(f"{lista[3][i][0]} -> {lista[3][i][1]} (Cruzamento)")

if __name__ == '__main__':
    global listaDeAdjacencia

    listaDeAdjacencia = carregarArquivo("T2.txt")
    listaDeGrau = criarListaDaGrau(listaDeAdjacencia)
    # print(listaDeGrau)
    # print(listaDeGrau)

    DFS(listaDeGrau)
