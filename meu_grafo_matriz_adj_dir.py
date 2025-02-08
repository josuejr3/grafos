from bibgrafo import aresta
from bibgrafo.grafo_matriz_adj_dir import *
from bibgrafo.grafo_errors import *
from copy import deepcopy

class MeuGrafo(GrafoMatrizAdjacenciaDirecionado):

    def vertices_nao_adjacentes(self):
        '''
        Provê uma lista de vértices não adjacentes no grafo. A lista terá o seguinte formato: [X-Z, X-W, ...]
        Onde X, Z e W são vértices no grafo que não tem uma aresta entre eles.
        :return: Uma lista com os pares de vértices não adjacentes
        '''
        pass

    def ha_laco(self):
        '''
        Verifica se existe algum laço no grafo.
        :return: Um valor booleano que indica se existe algum laço.
        '''
        pass


    def grau_entrada(self, V=''):
        '''
        Provê o grau do vértice passado como parâmetro
        :param V: O rótulo do vértice a ser analisado
        :return: Um valor inteiro que indica o grau do vértice
        :raises: VerticeInvalidoException se o vértice não existe no grafo
        '''
        pass

    def grau_saida(self, V=''):
        '''
        Provê o grau do vértice passado como parâmetro
        :param V: O rótulo do vértice a ser analisado
        :return: Um valor inteiro que indica o grau do vértice
        :raises: VerticeInvalidoException se o vértice não existe no grafo
        '''
        pass

    def ha_paralelas(self):
        '''
        Verifica se há arestas paralelas no grafo
        :return: Um valor booleano que indica se existem arestas paralelas no grafo.
        '''
        pass

    def arestas_sobre_vertice(self, V):
        '''
        Provê uma lista que contém os rótulos das arestas que incidem sobre o vértice passado como parâmetro
        :param V: O vértice a ser analisado
        :return: Uma lista os rótulos das arestas que incidem sobre o vértice
        :raises: VerticeInvalidoException se o vértice não existe no grafo
        '''
        if not self.existe_rotulo_vertice(V):
            raise VerticeInvalidoError("O vértice não existe no grafo")


        arestas_sob_o_vertice = list()

        # Encontra o índice na matriz
        indice_da_coluna_linha = self.indice_do_vertice(self.get_vertice(V))

        for i in range(len(self.matriz)):
            for j in range(len(self.matriz)):
                if i == indice_da_coluna_linha or j == indice_da_coluna_linha:
                    dic_arestas = self.matriz[indice_da_coluna_linha][j]
                    # alteração de add para dic_arestas[d]
                    for d in dic_arestas.keys():
                        aresta_adicionada = dic_arestas[d]
                        arestas_sob_o_vertice.append(aresta_adicionada)

        return arestas_sob_o_vertice


    def eh_completo(self):
        '''
        Verifica se o grafo é completo.
        :return: Um valor booleano que indica se o grafo é completo
        '''
        pass



    def warshall(self):
        '''
        Provê a matriz de alcançabilidade de Warshall do grafo
        :return: Uma lista de listas que representa a matriz de alcançabilidade de Warshall associada ao grafo
        '''

        matriz_e = deepcopy(self.matriz)
        matriz_booleana = [[1 if item else 0 for item in row] for row in matriz_e]

        qtd_vertices = len(matriz_booleana)

        for i in range(qtd_vertices):
            for j in range(qtd_vertices):
                if matriz_booleana[j][i] == 1:
                    for k in range(qtd_vertices):
                        matriz_booleana[j][k] = max(matriz_booleana[j][k], matriz_booleana[i][k])

        return matriz_booleana


    def remove_arestas_maiores(self):

        """
        Função que remove arestas paralelas de pesos maiores e laços
        """

        for i in range(len(self.matriz)):
            for j in range(len(self.matriz)):

                if i == j:
                    self.matriz[i][j].clear()

                if len(self.matriz[i][j]) > 1:
                    lista_arestas = self.matriz[i][j]
                    #menor_aresta = min(lista_arestas.values(), key=lambda aresta: aresta.peso)
                    while len(lista_arestas) > 1:
                        maior_aresta = max(lista_arestas.values(), key=lambda aresta_analisada: aresta_analisada.peso)
                        self.remove_aresta(maior_aresta.rotulo)

        return self

    def dijkstra(self, vi: str, vf: str) :

        """
        :param vi: vértice inicial
        :param vf: vértice final
        :return: uma lista com os vértices que formam o menor cominho
        :raises: VerticeInvalidoError se um dos vértices não existirem no grafo
        :raise: RuntimeError se não existir um caminho
        """

        # Conferindo se os dois vértices de entrada e saída existem
        if not self.existe_rotulo_vertice(vi) or not self.existe_rotulo_vertice(vf):
            raise VerticeInvalidoError

        # Definindo tamanho da matriz e os vertices
        dimensao_matriz = len(self.matriz)
        vertices = [v.rotulo for v in self.vertices]

        # Definindo caminho_ate, visitado e predecessor
        caminho_ate = {chave: "inf" for chave in vertices}; caminho_ate[vi] = 0
        visitado = {chave: 0 for chave in vertices}; visitado[vi] = 1
        predecessor = {chave: None for chave in vertices}

        # Definindo valor de w e o peso total do caminho
        w = vi

        while True:

            arestas_no_vertice = self.arestas_sobre_vertice(w)
            vertice = self.get_vertice(w)
            posicao_vertice = self.indice_do_vertice(vertice)

            if w == vf:
                menor_caminho = [vf]
                while menor_caminho[-1] != vi:
                    next_value = predecessor[vf]
                    menor_caminho.append(next_value)
                    if vf is not None:
                        vf = next_value
                menor_caminho.reverse()
                return menor_caminho
            elif sum(visitado.values()) == len(vertices) or not arestas_no_vertice:
                raise RuntimeError

            for i in range(dimensao_matriz):

                if posicao_vertice == i or len(self.matriz[posicao_vertice][i]) != 1:
                    continue

                aresta_analisada = list(self.matriz[posicao_vertice][i].values()) # Objeto Aresta na Lista   # UM UNICO OBJETO ARESTA
                aresta_analisada_real = aresta_analisada[0]

                # Propriedades Aresta
                aresta_rotulo = aresta_analisada_real.rotulo
                v1_aresta = aresta_analisada_real.v1.rotulo
                v2_aresta = aresta_analisada_real.v2.rotulo
                aresta_peso = aresta_analisada_real.peso

                # Atualizando os dos betas e colocando os predecessores
                if v1_aresta == w and aresta_rotulo:
                    if caminho_ate[v2_aresta] == "inf" or caminho_ate[v2_aresta] >= caminho_ate[v1_aresta] + aresta_peso:
                        caminho_ate[v2_aresta] = aresta_peso + caminho_ate[v1_aresta]
                        predecessor[v2_aresta] = w
                    arestas_no_vertice.remove(aresta_analisada_real)

                # Selecionando o menor valor de caminho_ate a partir dos tetas
                if not arestas_no_vertice:
                    menor_beta = min((v, k) for k, v in caminho_ate.items() if isinstance(v, int) and v != 0 and visitado[k] == 0)
                    menor_beta_vertice = menor_beta[1]
                    menor_beta_caminho = menor_beta[0]
                    caminho_ate[menor_beta_vertice] = menor_beta_caminho
                    w = menor_beta_vertice
                    visitado[w] = 1
                    break


    def bellman_ford(self, vi: str, vf: str) -> bool | list[str]:

        """
        Encontra o menor caminho entre dois vértices considerando pesos negativos
        :param vi: vértice inicial
        :param vf: vértice final
        :return: uma lista com os vértices que formam o menor caminho, ou False se o caminho não existir
        ou houver ciclos negativos
        :raises VerticeInvalidoError se um dos vértices não existir no grafo
        """


        # Verificando se os dois vértices existem.
        if not self.existe_rotulo_vertice(vi) or not self.existe_rotulo_vertice(vf):
            raise VerticeInvalidoError

        # Definindo tamanho da matriz e os vertices
        dimensao_matriz = len(self.matriz)
        vertices = [v.rotulo for v in self.vertices]


        beta = {chave: float("inf") for chave in vertices}; beta[vi] = 0
        predecessor = {chave: None for chave in vertices}

        arestas_totais = list()

        for i in range(len(vertices)):
            arestas_no_vertice = self.arestas_sobre_vertice(vertices[i])
            for a in arestas_no_vertice:
                if a not in arestas_totais:
                    arestas_totais.append(a)

        for k in range(dimensao_matriz - 1):

            for a in arestas_totais:

                # informações da aresta
                # aresta_rotulo = a.rotulo
                aresta_peso = a.peso
                v1_aresta = a.v1.rotulo
                v2_aresta = a.v2.rotulo

                # Se a aresta não possui valor, ela é pulada
                if beta[v1_aresta] == float("inf"):
                    continue

                if beta[v2_aresta] == float("inf") or beta[v2_aresta] > beta[v1_aresta] + aresta_peso:
                    beta[v2_aresta] = beta[v1_aresta] + aresta_peso
                    predecessor[v2_aresta] = v1_aresta

        # Laço para verificar se há ciclo negativo.

        for a in arestas_totais:
            if beta[a.v1.rotulo] != float("inf") and beta[a.v2.rotulo] > beta[a.v1.rotulo] + a.peso:
                return False

        if beta[vf] == float("inf"):
            return None

        # Construindo o menor caminho
        menor_caminho = list()
        atual = vf

        while atual is not None:
            menor_caminho.append(atual)
            atual = predecessor[atual]

        menor_caminho.reverse()
        return menor_caminho



















































