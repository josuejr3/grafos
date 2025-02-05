import random

from bibgrafo.grafo_lista_adj_nao_dir import GrafoListaAdjacenciaNaoDirecionado
from bibgrafo.grafo_errors import *


class MeuGrafo(GrafoListaAdjacenciaNaoDirecionado):

    def vertices_nao_adjacentes(self):
        '''
        Provê um conjunto de vértices não adjacentes no grafo.
        O conjunto terá o seguinte formato: {X-Z, X-W, ...}
        Onde X, Z e W são vértices no grafo que não tem uma aresta entre eles.
        :return: Um objeto do tipo set que contém os pares de vértices não adjacentes
        '''

        comb_possiveis: set[str] = set()
        arestas_adj: set[str] = set()

        for v in self.vertices:
            for u in self.vertices:
                str_aresta = f"{v}-{u}"
                if u != v:
                    if str_aresta[::-1] not in comb_possiveis:
                        comb_possiveis.add(str_aresta)

        for a in self.arestas:
            str_aresta_adj = f"{self.arestas[a].v1}-{self.arestas[a].v2}"
            arestas_adj.add(str_aresta_adj)
            arestas_adj.add(str_aresta_adj[::-1])

        resultado = comb_possiveis - arestas_adj
        return resultado

    def ha_laco(self):
        '''
        Verifica se existe algum laço no grafo.
        :return: Um valor booleano que indica se existe algum laço.
        '''



        for a in self.arestas:
            if self.arestas[a].v1 == self.arestas[a].v2:
                return True
        return False

    def grau(self, V=''):
        '''
        Provê o grau do vértice passado como parâmetro
        :param V: O rótulo do vértice a ser analisado
        :return: Um valor inteiro que indica o grau do vértice
        :raises: VerticeInvalidoError se o vértice não existe no grafo
        '''


        grau = 0

        if not self.existe_rotulo_vertice(V): raise VerticeInvalidoError("O vertice nao existe")

        for a in self.arestas:
            if self.arestas[a].v1.rotulo == V:
                grau += 1
            if self.arestas[a].v2.rotulo == V:
                grau += 1

        return grau

    def ha_paralelas(self):
        '''
        Verifica se há arestas paralelas no grafo
        :return: Um valor booleano que indica se existem arestas paralelas no grafo.
        '''


        for chave, valor in self.arestas.items():
            vertice_i = valor.v1.rotulo
            vertice_f = valor.v2.rotulo
            for chave2, valor_2 in self.arestas.items():
                if chave2 != chave:
                    if vertice_i == valor_2.v1.rotulo and vertice_f == valor_2.v2.rotulo:
                        return True
                    if vertice_f == valor_2.v1.rotulo and vertice_i == valor_2.v2.rotulo:
                        return True
        return False

    def arestas_sobre_vertice(self, V):
        '''
        Provê uma lista que contém os rótulos das arestas que incidem sobre o vértice passado como parâmetro
        :param V: Um string com o rótulo do vértice a ser analisado
        :return: Uma lista os rótulos das arestas que incidem sobre o vértice
        :raises: VerticeInvalidoException se o vértice não existe no grafo
        '''


        arestasIncidentes = set()

        if not self.existe_rotulo_vertice(V): raise VerticeInvalidoError("O vertice nao existe")

        for chave, valor in self.arestas.items():
            if valor.v1.rotulo == V or valor.v2.rotulo == V:
                if chave not in arestasIncidentes:
                    arestasIncidentes.add(chave)

        return arestasIncidentes

    def eh_completo(self):
        '''
        Verifica se o grafo é completo.
        :return: Um valor booleano que indica se o grafo é completo
        '''


        qtd_Vertices = len(self.vertices)
        qtd_Arestas = len(self.arestas)

        if qtd_Arestas == (qtd_Vertices*(qtd_Vertices-1) // 2) and not self.ha_paralelas() and not self.ha_laco(): return True
        return False

    def dfs(self, v=''):

        new_graph = MeuGrafo()

        if not self.existe_rotulo_vertice(v):
            raise VerticeInvalidoError
        new_graph.adiciona_vertice(v)

        def flux(root):

            incident_edges = sorted(list(self.arestas_sobre_vertice(root)))

            for edge in incident_edges:

                v1 = self.arestas[edge].v1.rotulo
                v2 = self.arestas[edge].v2.rotulo

                if new_graph.existe_rotulo_vertice(v1) and new_graph.existe_rotulo_vertice(v2):
                    continue

                if v1 != root:
                    next_vertex = v1
                else: next_vertex = v2

                new_graph.adiciona_vertice(next_vertex)
                new_graph.adiciona_aresta(self.arestas[edge])
                flux(next_vertex)

        flux(v)

        if len(self.vertices) != len(new_graph.vertices):
            return False
        return new_graph

    def bfs(self, v=''):

        new_graph = MeuGrafo()

        if not self.existe_rotulo_vertice(v):
            raise VerticeInvalidoError

        new_graph.adiciona_vertice(v)
        distance = list()
        distance.append(v)

        while distance:

            vertice = distance.pop(0)
            arestas_vertice = sorted(list(self.arestas_sobre_vertice(vertice)))

            for aresta in arestas_vertice:

                v1 = self.arestas[aresta].v1.rotulo
                v2 = self.arestas[aresta].v2.rotulo

                if new_graph.existe_rotulo_vertice(v1) and new_graph.existe_rotulo_vertice(v2):
                    continue

                prox_vrt = v1 if v1 != vertice else v2
                new_graph.adiciona_vertice(prox_vrt)
                new_graph.adiciona_aresta(self.arestas[aresta])
                distance.append(prox_vrt)

        if len(self.vertices) != len(new_graph.vertices):
            return False

        return new_graph

    def ha_ciclo(self):

        arestas_visitadas = set()
        vertices_visitados = set()
        caminho = list()

        # Cria uma lista com todos os vértices do grafo
        vertices = [str(v) for v in self.vertices]

        # Função que percorre o grafo
        def fluxo(v):

            arestas_sob_o_vertice = sorted(list(self.arestas_sobre_vertice(v)))

            # Se o vértice analisado não possui arestas ele passa para próximo vértice
            if len(arestas_sob_o_vertice) <= 1:
                if caminho:
                    caminho.pop()
                    caminho.pop()
                return

            # Percorre as arestas do grafo
            for aresta in arestas_sob_o_vertice:

                # Verifica se o tamanho do caminho é duas vezes maior que o tamanho passado
                # (lista comporta as arestas e vertices)

                if len(caminho) >= 3 and caminho[0] == caminho[-1]:
                        return caminho

                # Define os vértices da aresta analisada
                v1 = self.arestas[aresta].v1.rotulo
                v2 = self.arestas[aresta].v2.rotulo

                # Se os vértices já estão no caminho ou aresta já foi visitada ela é ignorada e passa para a próxima

                if (v1 in caminho or v2 in caminho) and aresta in arestas_visitadas and caminho[0] != caminho[-1]:
                    continue

                # Definição do próximo vértice a ser análisado
                if v1 != v:
                    next_v = v1
                else:
                    next_v = v2

                if v not in caminho:
                    caminho.append(v)

                if v1 != v2:
                    caminho.append(aresta)
                    arestas_visitadas.add(aresta)
                    vertices_visitados.add(v)
                    caminho.append(next_v)

                if v1 == v2:
                    arestas_visitadas.add(aresta)
                    vertices_visitados.add(v)
                    continue

                # Após atualizado o caminho e as arestas visitadas verifica-se novamente
                # se o tamanho do caminho foi atingido
                if len(caminho) >= 3 and caminho[0] == caminho[-1]:
                    break
                else:
                    fluxo(next_v)

            arestas_visitadas.clear()
            if len(caminho) >= 3 and caminho[0] == caminho[-1]:
                return caminho


            caminho.pop()
            caminho.pop()

            return caminho

        try:
            # Percorre os vértices e verifica se eles possuem caminhos.
            for v in vertices:
                if fluxo(v):
                    return fluxo(v)
                else:
                    continue
            return False
        except IndexError:
            return False

    def conexo(self):

        eh_conexo = False

        for v in self.vertices:
            grafo_resultante = self.bfs(v.rotulo)
            if grafo_resultante and (len(grafo_resultante.vertices)) > 1:
                eh_conexo = True
            else:
                eh_conexo = False
        return eh_conexo

    def caminho(self, n):

        # Verifica se o tamanho do caminho é válido
        if n < 1:
            return False

        arestas_visitadas = set()
        vertices_visitados = set()
        caminho = list()

        # Cria uma lista com todos os vértices do grafo
        vertices = [str(v) for v in self.vertices]

        # Função que percorre o grafo
        def fluxo(v, tamanho):

            arestas_sob_o_vertice = sorted(list(self.arestas_sobre_vertice(v)))

            # Se o vértice analisado não possui arestas ele passa para próximo vértice
            if not arestas_sob_o_vertice:
                return

            # Percorre as arestas do grafo
            for aresta in arestas_sob_o_vertice:

                # Verifica se o tamanho do caminho é duas vezes maior que o tamanho passado
                # (lista comporta as arestas e vertices)

                if len(caminho) >= (2 * tamanho):
                    return caminho

                # Define os vértices da aresta analisada
                v1 = self.arestas[aresta].v1.rotulo
                v2 = self.arestas[aresta].v2.rotulo

                # Se os vértices já estão no caminho ou aresta já foi visitada ela é ignorada e passa para a próxima
                if (v1 in caminho and v2 in caminho) or aresta in arestas_visitadas:
                    continue

                # Definição do próximo vértice a ser análisado
                if v1 != v:
                    next_v = v1
                else:
                    next_v = v2

                if v not in caminho:
                    caminho.append(v)

                if v1 != v2:
                    caminho.append(aresta)
                    caminho.append(next_v)

                arestas_visitadas.add(aresta)
                vertices_visitados.add(v)

                if v1 == v2:
                    continue

                # Após atualizado o caminho e as arestas visitadas verifica-se novamente
                # se o tamanho do caminho foi atingido
                if len(caminho) == (2*tamanho):
                    break
                else:
                    fluxo(next_v, tamanho)

            arestas_visitadas.clear()
            if len(caminho) >= (2*tamanho):
                return caminho

            caminho.pop()
            caminho.pop()
            return caminho

        try:
            # Percorre os vértices e verifica se eles possuem caminhos.
            for v in vertices:
                if fluxo(v, n):
                    return fluxo(v, n)
                else:
                    continue
            return False
        except IndexError:
            return False











































