from bibgrafo.grafo_matriz_adj_nao_dir import GrafoMatrizAdjacenciaNaoDirecionado
from bibgrafo.grafo_errors import *


class MeuGrafo(GrafoMatrizAdjacenciaNaoDirecionado):

    def vertices_nao_adjacentes(self):
        '''
        Provê um conjunto (set) de vértices não adjacentes no grafo.
        O conjunto terá o seguinte formato: {X-Z, X-W, ...}
        Onde X, Z e W são vértices no grafo que não tem uma aresta entre eles.
        :return: Um conjunto (set) com os pares de vértices não adjacentes
        '''


        vertices_n_adjacentes = set()

        for i in range(len(self.matriz)):
            for j in range(len(self.matriz)):
                if len(self.matriz[i][j]) == 0:
                    v1 = self.vertices[i].rotulo
                    v2 = self.vertices[j].rotulo

                    if v1 != v2:
                        if not f"{v2}-{v1}" in vertices_n_adjacentes:
                            vertices_n_adjacentes.add(f"{v1}-{v2}")

        return set(sorted(vertices_n_adjacentes))
        # sempre tenho que converter de novo pra set?

    def ha_laco(self):
        '''
        Verifica se existe algum laço no grafo.
        :return: Um valor booleano que indica se existe algum laço.
        '''

        for i in range(len(self.matriz)):
            if len(self.matriz[i][i]) > 0:
                    return True
        return False


    def grau(self, V=''):
        '''
        Provê o grau do vértice passado como parâmetro
        :param V: O rótulo do vértice a ser analisado
        :return: Um valor inteiro que indica o grau do vértice
        :raises: VerticeInvalidoError se o vértice não existe no grafo
        '''

        if not self.existe_rotulo_vertice(V):
            raise VerticeInvalidoError("O vertice não existe no grafo")


        # Percorrer uma linha ou uma coluna

        # Enconta o indice na lista de vertices
        indice_da_coluna_linha = self.indice_do_vertice(self.get_vertice(V))

        grau_vertice = 0

        for i in range(len(self.matriz)):
            for j in range(len(self.matriz)):
                if i == indice_da_coluna_linha:
                    dic_arestas = self.matriz[i][j]
                    for aresta in dic_arestas:
                        if dic_arestas[aresta].v1.rotulo == dic_arestas[aresta].v2.rotulo:
                            grau_vertice+=2
                        else:
                            grau_vertice+=1

        return grau_vertice
        # Forma de fazer sem usar 3 For


    def ha_paralelas(self):
        '''
        Verifica se há arestas paralelas no grafo
        :return: Um valor booleano que indica se existem arestas paralelas no grafo.
        '''

        for i in range(len(self.matriz)):
            for j in range(len(self.matriz)):
                # quantidade de dicionarios aresta-vertice
                if len(self.matriz[i][j]) >= 2:
                    return True
        return False



    def arestas_sobre_vertice(self, V):
        '''
        Provê um conjunto (set) que contém os rótulos das arestas que
        incidem sobre o vértice passado como parâmetro
        :param V: O vértice a ser analisado
        :return: Um conjunto com os rótulos das arestas que incidem sobre o vértice
        :raises: VerticeInvalidoError se o vértice não existe no grafo
        '''

        if not self.existe_rotulo_vertice(V):
            raise VerticeInvalidoError("O vértice não existe no grafo")


        arestas_sob_o_vertice = set()

        # Encontra o índice na matriz
        indice_da_coluna_linha = self.indice_do_vertice(self.get_vertice(V))

        for i in range(len(self.matriz)):
            for j in range(len(self.matriz)):
                if i == indice_da_coluna_linha or j == indice_da_coluna_linha:
                    dic_arestas = self.matriz[indice_da_coluna_linha][j]

                    for d in dic_arestas:
                        arestas_sob_o_vertice.add(d)

        return arestas_sob_o_vertice

    def eh_completo(self):
        '''
        Verifica se o grafo é completo.
        :return: Um valor booleano que indica se o grafo é completo
        '''

        if self.ha_laco() or self.ha_paralelas():
            return False

        for i in range(len(self.matriz)):
            for j in range(len(self.matriz)):
                if i != j:
                    if len(self.matriz[i][j]) == 0:
                        return False
        return True