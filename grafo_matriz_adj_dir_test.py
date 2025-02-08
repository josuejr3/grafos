import unittest
from bibgrafo.aresta import ArestaDirecionada
from bibgrafo.grafo_errors import VerticeInvalidoError, ArestaInvalidaError
from bibgrafo.grafo_json import GrafoJSON
from bibgrafo.grafo_builder import GrafoBuilder
from meu_grafo_matriz_adj_dir import *

class TestGrafo(unittest.TestCase):

    def setUp(self):
        # Grafo da Paraíba
        self.g_p = GrafoJSON.json_to_grafo('test_json/grafo_pb.json', MeuGrafo())

        # Clone do Grafo da Paraíba para ver se o método equals está funcionando
        self.g_p2 = GrafoJSON.json_to_grafo('test_json/grafo_pb2.json', MeuGrafo())

        # Outro clone do Grafo da Paraíba para ver se o método equals está funcionando
        # Esse tem um pequena diferença na primeira aresta
        self.g_p3 = GrafoJSON.json_to_grafo('test_json/grafo_pb3.json', MeuGrafo())

        # Outro clone do Grafo da Paraíba para ver se o método equals está funcionando
        # Esse tem um pequena diferença na segunda aresta
        self.g_p4 = GrafoJSON.json_to_grafo('test_json/grafo_pb4.json', MeuGrafo())

        # Grafo da Paraíba sem arestas paralelas
        self.g_p_sem_paralelas = GrafoJSON.json_to_grafo('test_json/grafo_pb_simples.json', MeuGrafo())

        # Grafos completos
        self.g_c = GrafoBuilder().tipo(MeuGrafo()) \
            .vertices(['J', 'C', 'E', 'P']).arestas(True).build()

        self.g_c2 = GrafoBuilder().tipo(MeuGrafo()) \
            .vertices(3).arestas(True).build()

        self.g_c3 = GrafoBuilder().tipo(MeuGrafo()) \
            .vertices(1).build()


        # Grafos com laco
        self.g_l1 = GrafoJSON.json_to_grafo('test_json/grafo_l1.json', MeuGrafo())

        self.g_l2 = GrafoJSON.json_to_grafo('test_json/grafo_l2.json', MeuGrafo())

        self.g_l3 = GrafoJSON.json_to_grafo('test_json/grafo_l3.json', MeuGrafo())

        self.g_l4 = GrafoBuilder().tipo(MeuGrafo()).vertices([(v:=Vertice('D'))]) \
            .arestas([ArestaDirecionada('a1', v, v)]).build()

        self.g_l5 = GrafoBuilder().tipo(MeuGrafo()).vertices(3) \
            .arestas(3, lacos=1).build()

        # Grafos desconexos
        self.g_d = GrafoBuilder().tipo(MeuGrafo()) \
            .vertices([a:=Vertice('A'), b:=Vertice('B'), Vertice('C'), Vertice('D')]) \
            .arestas([ArestaDirecionada('asd', a, b)]).build()

        self.g_d2 = GrafoBuilder().tipo(MeuGrafo()).vertices(4).build()

        # Grafo com ciclos e laços
        self.g_e = MeuGrafo()
        self.g_e.adiciona_vertice("A")
        self.g_e.adiciona_vertice("B")
        self.g_e.adiciona_vertice("C")
        self.g_e.adiciona_vertice("D")
        self.g_e.adiciona_vertice("E")
        self.g_e.adiciona_aresta('1', 'A', 'B')
        self.g_e.adiciona_aresta('2', 'A', 'C')
        self.g_e.adiciona_aresta('3', 'C', 'A')
        self.g_e.adiciona_aresta('4', 'C', 'B')
        self.g_e.adiciona_aresta('10', 'C', 'B')
        self.g_e.adiciona_aresta('5', 'C', 'D')
        self.g_e.adiciona_aresta('6', 'D', 'D')
        self.g_e.adiciona_aresta('7', 'D', 'B')
        self.g_e.adiciona_aresta('8', 'D', 'E')
        self.g_e.adiciona_aresta('9', 'E', 'A')
        self.g_e.adiciona_aresta('11', 'E', 'B')

        # Matrizes Warshall

        # Matriz Grafo da Paraíba
        self.g_p_matriz = self.cria_matriz(self.g_p)
        self.g_p_matriz[0][1] = 1
        self.g_p_matriz[0][2] = 1
        self.g_p_matriz[1][2] = 1
        self.g_p_matriz[3][1] = 1
        self.g_p_matriz[3][2] = 1
        self.g_p_matriz[4][1] = 1
        self.g_p_matriz[4][2] = 1
        self.g_p_matriz[4][5] = 1
        self.g_p_matriz[4][6] = 1
        self.g_p_matriz[5][1] = 1
        self.g_p_matriz[5][2] = 1
        self.g_p_matriz[5][6] = 1

        # Matriz Grafo da Paraíba sem Paralelas
        self.g_p_sem_paralelas_matriz = self.cria_matriz(self.g_p_sem_paralelas)
        self.g_p_sem_paralelas_matriz[0][1] = 1
        self.g_p_sem_paralelas_matriz[0][2] = 1
        self.g_p_sem_paralelas_matriz[1][2] = 1
        self.g_p_sem_paralelas_matriz[3][1] = 1
        self.g_p_sem_paralelas_matriz[3][2] = 1
        self.g_p_sem_paralelas_matriz[4][1] = 1
        self.g_p_sem_paralelas_matriz[4][2] = 1
        self.g_p_sem_paralelas_matriz[4][5] = 1
        self.g_p_sem_paralelas_matriz[4][6] = 1
        self.g_p_sem_paralelas_matriz[5][1] = 1
        self.g_p_sem_paralelas_matriz[5][2] = 1
        self.g_p_sem_paralelas_matriz[5][6] = 1

        # Grafo Completo K4
        self.g_k4 = MeuGrafo()
        self.g_k4.adiciona_vertice("A")
        self.g_k4.adiciona_vertice("B")
        self.g_k4.adiciona_vertice("C")
        self.g_k4.adiciona_vertice("D")
        self.g_k4.adiciona_aresta("a1", "A", "B")
        self.g_k4.adiciona_aresta("a2", "A", "C")
        self.g_k4.adiciona_aresta("a3", "A", "D")
        self.g_k4.adiciona_aresta("a4", "C", "B")
        self.g_k4.adiciona_aresta("a5", "D", "B")
        self.g_k4.adiciona_aresta("a6", "D", "C")

        # Matriz K4
        self.g_k4_matriz = self.cria_matriz(self.g_k4)
        self.g_k4_matriz[0][1] = 1
        self.g_k4_matriz[0][2] = 1
        self.g_k4_matriz[0][3] = 1
        self.g_k4_matriz[2][1] = 1
        self.g_k4_matriz[3][1] = 1
        self.g_k4_matriz[3][2] = 1

        # Grafo com ciclos
        self.g_c_c = MeuGrafo()
        self.g_c_c.adiciona_vertice("U")
        self.g_c_c.adiciona_vertice("V")
        self.g_c_c.adiciona_vertice("W")
        self.g_c_c.adiciona_vertice("X")
        self.g_c_c.adiciona_vertice("Y")
        self.g_c_c.adiciona_aresta("a1", "U", "Y")
        self.g_c_c.adiciona_aresta("a2", "Y", "V")
        self.g_c_c.adiciona_aresta("a3", "V", "U")
        self.g_c_c.adiciona_aresta("a4", "W", "X")

        self.g_c_c_matriz = self.cria_matriz(self.g_c_c)
        self.g_c_c_matriz[0][0] = 1
        self.g_c_c_matriz[0][1] = 1
        self.g_c_c_matriz[0][4] = 1
        self.g_c_c_matriz[1][0] = 1
        self.g_c_c_matriz[1][1] = 1
        self.g_c_c_matriz[1][4] = 1
        self.g_c_c_matriz[2][3] = 1
        self.g_c_c_matriz[4][0] = 1
        self.g_c_c_matriz[4][1] = 1
        self.g_c_c_matriz[4][4] = 1

        # Grafo com laço e arestas paralelas
        self.grafo_ap_l_1 = MeuGrafo()
        self.grafo_ap_l_1.adiciona_vertice("A")
        self.grafo_ap_l_1.adiciona_vertice("B")
        self.grafo_ap_l_1.adiciona_vertice("C")
        self.grafo_ap_l_1.adiciona_vertice("D")
        self.grafo_ap_l_1.adiciona_vertice("E")
        self.grafo_ap_l_1.adiciona_aresta("a1", "A", "B")
        self.grafo_ap_l_1.adiciona_aresta("a2", "A", "C")
        self.grafo_ap_l_1.adiciona_aresta("a3", "B", "A")
        self.grafo_ap_l_1.adiciona_aresta("a4", "B", "C")
        self.grafo_ap_l_1.adiciona_aresta("a5", "C", "C")
        self.grafo_ap_l_1.adiciona_aresta("a6", "D", "D")
        self.grafo_ap_l_1.adiciona_aresta("a7", "D", "A")
        self.grafo_ap_l_1.adiciona_aresta("a8", "E", "B")

        self.grafo_ap_l_1_matriz = self.cria_matriz(self.grafo_ap_l_1)
        self.grafo_ap_l_1_matriz[0][0] = 1
        self.grafo_ap_l_1_matriz[0][1] = 1
        self.grafo_ap_l_1_matriz[0][2] = 1
        self.grafo_ap_l_1_matriz[1][0] = 1
        self.grafo_ap_l_1_matriz[1][1] = 1
        self.grafo_ap_l_1_matriz[1][2] = 1
        self.grafo_ap_l_1_matriz[2][2] = 1
        self.grafo_ap_l_1_matriz[3][0] = 1
        self.grafo_ap_l_1_matriz[3][1] = 1
        self.grafo_ap_l_1_matriz[3][2] = 1
        self.grafo_ap_l_1_matriz[3][3] = 1
        self.grafo_ap_l_1_matriz[4][0] = 1
        self.grafo_ap_l_1_matriz[4][1] = 1
        self.grafo_ap_l_1_matriz[4][2] = 1

        self.g_e_matriz = self.cria_matriz(self.g_e)
        self.g_e_matriz[0][0] = 1
        self.g_e_matriz[0][1] = 1
        self.g_e_matriz[0][2] = 1
        self.g_e_matriz[0][3] = 1
        self.g_e_matriz[0][4] = 1
        self.g_e_matriz[2][0] = 1
        self.g_e_matriz[2][1] = 1
        self.g_e_matriz[2][2] = 1
        self.g_e_matriz[2][3] = 1
        self.g_e_matriz[2][4] = 1
        self.g_e_matriz[3][0] = 1
        self.g_e_matriz[3][1] = 1
        self.g_e_matriz[3][2] = 1
        self.g_e_matriz[3][3] = 1
        self.g_e_matriz[3][4] = 1
        self.g_e_matriz[4][0] = 1
        self.g_e_matriz[4][1] = 1
        self.g_e_matriz[4][2] = 1
        self.g_e_matriz[4][3] = 1
        self.g_e_matriz[4][4] = 1

        # Grafo com varios laços
        self.g_c_l_2 = MeuGrafo()
        self.g_c_l_2.adiciona_vertice("A")
        self.g_c_l_2.adiciona_vertice("B")
        self.g_c_l_2.adiciona_vertice("C")
        self.g_c_l_2.adiciona_vertice("D")
        self.g_c_l_2.adiciona_vertice("E")
        self.g_c_l_2.adiciona_vertice("F")
        self.g_c_l_2.adiciona_aresta("a1", "A", "A")
        self.g_c_l_2.adiciona_aresta("a2", "A", "B")
        self.g_c_l_2.adiciona_aresta("a3", "B", "C")
        self.g_c_l_2.adiciona_aresta("a4", "C", "B")
        self.g_c_l_2.adiciona_aresta("a5", "C", "E")
        self.g_c_l_2.adiciona_aresta("a6", "C", "D")
        self.g_c_l_2.adiciona_aresta("a7", "D", "D")
        self.g_c_l_2.adiciona_aresta("a8", "E", "E")

        self.g_c_l_2_matriz = self.cria_matriz(self.g_c_l_2)
        self.g_c_l_2_matriz[0][0] = 1
        self.g_c_l_2_matriz[0][1] = 1
        self.g_c_l_2_matriz[0][2] = 1
        self.g_c_l_2_matriz[0][3] = 1
        self.g_c_l_2_matriz[0][4] = 1
        self.g_c_l_2_matriz[1][1] = 1
        self.g_c_l_2_matriz[1][2] = 1
        self.g_c_l_2_matriz[1][3] = 1
        self.g_c_l_2_matriz[1][4] = 1
        self.g_c_l_2_matriz[2][1] = 1
        self.g_c_l_2_matriz[2][2] = 1
        self.g_c_l_2_matriz[2][3] = 1
        self.g_c_l_2_matriz[2][4] = 1
        self.g_c_l_2_matriz[3][3] = 1
        self.g_c_l_2_matriz[4][4] = 1

        self.g_l1_matriz = self.cria_matriz(self.g_l1)
        self.g_l1_matriz[0][0] = 1
        self.g_l1_matriz[1][0] = 1

        self.g_ap_l_2 = MeuGrafo()
        self.g_ap_l_2.adiciona_vertice("A")
        self.g_ap_l_2.adiciona_vertice("B")
        self.g_ap_l_2.adiciona_vertice("C")
        self.g_ap_l_2.adiciona_vertice("D")
        self.g_ap_l_2.adiciona_vertice("E")
        self.g_ap_l_2.adiciona_vertice("F")
        self.g_ap_l_2.adiciona_vertice("G")
        self.g_ap_l_2.adiciona_vertice("H")
        self.g_ap_l_2.adiciona_aresta("a1", "A", "B")
        self.g_ap_l_2.adiciona_aresta("a2", "A", "D")
        self.g_ap_l_2.adiciona_aresta("a3", "A", "E")
        self.g_ap_l_2.adiciona_aresta("a4", "B", "E")
        self.g_ap_l_2.adiciona_aresta("a5", "C", "B")
        self.g_ap_l_2.adiciona_aresta("a6", "C", "G")
        self.g_ap_l_2.adiciona_aresta("a7", "D", "A")
        self.g_ap_l_2.adiciona_aresta("a8", "D", "C")
        self.g_ap_l_2.adiciona_aresta("a9", "D", "F")
        self.g_ap_l_2.adiciona_aresta("a10", "F", "F")
        self.g_ap_l_2.adiciona_aresta("a11", "G", "D")
        self.g_ap_l_2.adiciona_aresta("a12", "G", "G")
        self.g_ap_l_2.adiciona_aresta("a13", "H", "E")
        self.g_ap_l_2.adiciona_aresta("a14", "H", "H")


        # Matriz grafo g_ap_l_2
        self.g_ap_l_2_matriz = self.cria_matriz(self.g_ap_l_2)
        self.g_ap_l_2_matriz[0][0] = 1
        self.g_ap_l_2_matriz[0][1] = 1
        self.g_ap_l_2_matriz[0][2] = 1
        self.g_ap_l_2_matriz[0][3] = 1
        self.g_ap_l_2_matriz[0][4] = 1
        self.g_ap_l_2_matriz[0][5] = 1
        self.g_ap_l_2_matriz[0][6] = 1
        self.g_ap_l_2_matriz[1][4] = 1
        self.g_ap_l_2_matriz[2][0] = 1
        self.g_ap_l_2_matriz[2][1] = 1
        self.g_ap_l_2_matriz[2][2] = 1
        self.g_ap_l_2_matriz[2][3] = 1
        self.g_ap_l_2_matriz[2][4] = 1
        self.g_ap_l_2_matriz[2][5] = 1
        self.g_ap_l_2_matriz[2][6] = 1
        self.g_ap_l_2_matriz[3][0] = 1
        self.g_ap_l_2_matriz[3][1] = 1
        self.g_ap_l_2_matriz[3][2] = 1
        self.g_ap_l_2_matriz[3][3] = 1
        self.g_ap_l_2_matriz[3][4] = 1
        self.g_ap_l_2_matriz[3][5] = 1
        self.g_ap_l_2_matriz[3][6] = 1
        self.g_ap_l_2_matriz[5][5] = 1
        self.g_ap_l_2_matriz[6][0] = 1
        self.g_ap_l_2_matriz[6][1] = 1
        self.g_ap_l_2_matriz[6][2] = 1
        self.g_ap_l_2_matriz[6][3] = 1
        self.g_ap_l_2_matriz[6][4] = 1
        self.g_ap_l_2_matriz[6][5] = 1
        self.g_ap_l_2_matriz[6][6] = 1
        self.g_ap_l_2_matriz[7][4] = 1
        self.g_ap_l_2_matriz[7][7] = 1

        # grafo arestas paralelas e laços
        self.g_ap_l_3 = MeuGrafo()
        self.g_ap_l_3.adiciona_vertice("A")
        self.g_ap_l_3.adiciona_vertice("B")
        self.g_ap_l_3.adiciona_vertice("C")
        self.g_ap_l_3.adiciona_aresta('a1', 'A', 'A')
        self.g_ap_l_3.adiciona_aresta('a2', 'B', 'B')
        self.g_ap_l_3.adiciona_aresta('a3', 'C', 'C')
        self.g_ap_l_3.adiciona_aresta('a4', 'A', 'B')
        self.g_ap_l_3.adiciona_aresta('a5', 'B', 'A')
        self.g_ap_l_3.adiciona_aresta('a6', 'B', 'C')
        self.g_ap_l_3.adiciona_aresta('a7', 'C', 'B')
        self.g_ap_l_3.adiciona_aresta('a8', 'C', 'A')
        self.g_ap_l_3.adiciona_aresta('a9', 'A', 'C')

        self.g_ap_l_3_matriz = self.cria_matriz(self.g_ap_l_3)
        self.g_ap_l_3_matriz[0][0] = 1
        self.g_ap_l_3_matriz[0][1] = 1
        self.g_ap_l_3_matriz[0][2] = 1
        self.g_ap_l_3_matriz[1][0] = 1
        self.g_ap_l_3_matriz[1][1] = 1
        self.g_ap_l_3_matriz[1][2] = 1
        self.g_ap_l_3_matriz[2][0] = 1
        self.g_ap_l_3_matriz[2][1] = 1
        self.g_ap_l_3_matriz[2][2] = 1

        # Grafos Dijkstra
        self.grafo_1 = MeuGrafo()
        self.grafo_1.adiciona_vertice("A")
        self.grafo_1.adiciona_vertice("B")
        self.grafo_1.adiciona_vertice("C")
        self.grafo_1.adiciona_vertice("D")
        self.grafo_1.adiciona_vertice("E")
        self.grafo_1.adiciona_aresta("a1", "A", "C", 5)
        self.grafo_1.adiciona_aresta("a2", "A", "B", 2)
        self.grafo_1.adiciona_aresta("a3", "B", "C", 1)
        self.grafo_1.adiciona_aresta("a4", "B", "D", 4)
        self.grafo_1.adiciona_aresta("a5", "C", "E", 3)
        self.grafo_1.adiciona_aresta("a6", "D", "E", 2)

        self.grafo_2 = MeuGrafo()
        self.grafo_2.adiciona_vertice("A")
        self.grafo_2.adiciona_vertice("B")
        self.grafo_2.adiciona_vertice("C")
        self.grafo_2.adiciona_vertice("D")
        self.grafo_2.adiciona_vertice("E")
        self.grafo_2.adiciona_vertice("F")
        self.grafo_2.adiciona_vertice("G")
        self.grafo_2.adiciona_vertice("H")
        self.grafo_2.adiciona_aresta('a1', 'A', 'B', 6)
        self.grafo_2.adiciona_aresta('a2', 'A', 'C', 4)
        self.grafo_2.adiciona_aresta('a3', 'B', 'D', 5)
        self.grafo_2.adiciona_aresta('a4', 'B', 'H', 2)
        self.grafo_2.adiciona_aresta('a5', 'C', 'D', 3)
        self.grafo_2.adiciona_aresta('a6', 'C', 'B', 1)
        self.grafo_2.adiciona_aresta('a7', 'D', 'E', 3)
        self.grafo_2.adiciona_aresta('a8', 'D', 'F', 1)
        self.grafo_2.adiciona_aresta('a9', 'F', 'G', 1)
        self.grafo_2.adiciona_aresta('a10', 'G', 'E', 2)
        self.grafo_2.adiciona_aresta('a11', 'H', 'G', 3)

        self.grafo_3 = MeuGrafo()
        self.grafo_3.adiciona_vertice("A")
        self.grafo_3.adiciona_vertice("B")
        self.grafo_3.adiciona_vertice("C")
        self.grafo_3.adiciona_vertice("D")
        self.grafo_3.adiciona_vertice("E")
        self.grafo_3.adiciona_vertice("F")
        self.grafo_3.adiciona_aresta("a1", "A", "B", 2)
        self.grafo_3.adiciona_aresta("a2", "A", "C", 4)
        self.grafo_3.adiciona_aresta("a3", "B", "C", 1)
        self.grafo_3.adiciona_aresta("a4", "B", "D", 4)
        self.grafo_3.adiciona_aresta("a5", "B", "E", 3)
        self.grafo_3.adiciona_aresta("a6", "C", "E", 1)
        self.grafo_3.adiciona_aresta("a7", "D", "F", 2)
        self.grafo_3.adiciona_aresta("a8", "E", "D", 3)
        self.grafo_3.adiciona_aresta("a9", "E", "F", 1)

        self.grafo_2bf = MeuGrafo()
        self.grafo_2bf.adiciona_vertice("A")
        self.grafo_2bf.adiciona_vertice("B")
        self.grafo_2bf.adiciona_vertice("C")
        self.grafo_2bf.adiciona_vertice("D")
        self.grafo_2bf.adiciona_vertice("E")
        self.grafo_2bf.adiciona_vertice("F")
        self.grafo_2bf.adiciona_aresta('a1', 'A', 'B', 2)
        self.grafo_2bf.adiciona_aresta('a2', 'C', 'A', 1)
        self.grafo_2bf.adiciona_aresta('a3', 'C', 'B', 3)
        self.grafo_2bf.adiciona_aresta('a4', 'D', 'A', 1)
        self.grafo_2bf.adiciona_aresta('a5', 'D', 'C', 2)
        self.grafo_2bf.adiciona_aresta("a6", 'E', 'D', 5)
        self.grafo_2bf.adiciona_aresta("a7", 'E', 'C', 10)
        self.grafo_2bf.adiciona_aresta("a8", 'E', 'F', 4)
        self.grafo_2bf.adiciona_aresta("a9", 'F', 'A', 5)
        self.grafo_2bf.adiciona_aresta("a10", 'F', 'D', 1)

        self.grafo_5 = MeuGrafo()
        self.grafo_5.adiciona_vertice("1")
        self.grafo_5.adiciona_vertice("2")
        self.grafo_5.adiciona_vertice("3")
        self.grafo_5.adiciona_vertice("4")
        self.grafo_5.adiciona_vertice("5")
        self.grafo_5.adiciona_vertice("6")
        self.grafo_5.adiciona_aresta('a1', '1', '2', 7)
        self.grafo_5.adiciona_aresta('a2', '1', '3', 9)
        self.grafo_5.adiciona_aresta('a3', '1', '6', 14)
        self.grafo_5.adiciona_aresta('a4', '2', '3', 10)
        self.grafo_5.adiciona_aresta('a5', '2', '4', 15)
        self.grafo_5.adiciona_aresta('a6', '3', '4', 11)
        self.grafo_5.adiciona_aresta('a7', '3', '6', 2)
        self.grafo_5.adiciona_aresta('a8', '6', '5', 9)
        self.grafo_5.adiciona_aresta("a9", '4', '5', 6)

        self.grafo_6 = MeuGrafo()
        self.grafo_6.adiciona_vertice('0')
        self.grafo_6.adiciona_vertice('1')
        self.grafo_6.adiciona_vertice('2')
        self.grafo_6.adiciona_vertice('3')
        self.grafo_6.adiciona_vertice('4')
        self.grafo_6.adiciona_vertice('5')
        self.grafo_6.adiciona_vertice('6')
        self.grafo_6.adiciona_vertice('7')
        self.grafo_6.adiciona_aresta('a1', '0', '2', 26)
        self.grafo_6.adiciona_aresta('a2', '0', '4', 38)
        self.grafo_6.adiciona_aresta('a3', '1', '3', 29)
        self.grafo_6.adiciona_aresta('a4', '2', '7', 34)
        self.grafo_6.adiciona_aresta('a5', '3', '6', 52)
        self.grafo_6.adiciona_aresta('a6', '4', '7', 37)
        self.grafo_6.adiciona_aresta('a7', '4', '5', 35)
        self.grafo_6.adiciona_aresta('a8', '5', '4', 35)
        self.grafo_6.adiciona_aresta('a9', '5', '7', 28)
        self.grafo_6.adiciona_aresta('a10', '5', '1', 32)
        self.grafo_6.adiciona_aresta('a11', '6', '2', 40)
        self.grafo_6.adiciona_aresta('a12', '6', '0', 58)
        self.grafo_6.adiciona_aresta('a13', '6', '4', 93)
        self.grafo_6.adiciona_aresta('a14', '7', '5', 28)
        self.grafo_6.adiciona_aresta('a15', '7', '3', 39)

        self.grafo_7 = MeuGrafo()
        self.grafo_7.adiciona_vertice('A')
        self.grafo_7.adiciona_vertice('B')
        self.grafo_7.adiciona_vertice('C')
        self.grafo_7.adiciona_vertice('D')
        self.grafo_7.adiciona_vertice('E')
        self.grafo_7.adiciona_vertice('F')
        self.grafo_7.adiciona_vertice('G')
        self.grafo_7.adiciona_vertice('H')
        self.grafo_7.adiciona_vertice('T')
        self.grafo_7.adiciona_aresta('a1', 'A', 'F', 24)
        self.grafo_7.adiciona_aresta('a2', 'A', 'E', 70)
        self.grafo_7.adiciona_aresta('a3', 'D', 'H', 29)
        self.grafo_7.adiciona_aresta('a4', 'G', 'H', 66)
        self.grafo_7.adiciona_aresta('a5', 'F', 'D', 120)
        self.grafo_7.adiciona_aresta('a6', 'E', 'G', 42)
        self.grafo_7.adiciona_aresta('a7', 'A', 'C', 47)
        self.grafo_7.adiciona_aresta('a8', 'C', 'B', 55)
        self.grafo_7.adiciona_aresta('a9', 'B', 'H', 79)
        self.grafo_7.adiciona_aresta('a10', 'F', 'C', 25)
        self.grafo_7.adiciona_aresta('a11', 'C', 'E', 23)
        self.grafo_7.adiciona_aresta('a12', 'B', 'D', 31)
        self.grafo_7.adiciona_aresta('a13', 'B', 'G', 74)
        self.grafo_7.adiciona_aresta('a14', 'E', 'B', 31)
        self.grafo_7.adiciona_aresta('a15', 'C', 'G', 66)
        self.grafo_7.adiciona_aresta('a16', 'C', 'D', 88)

        # Grafos para teste Bellman-Ford

        # Grafo visto em sala de aula
        self.grafo_1bf = MeuGrafo()
        self.grafo_1bf.adiciona_vertice('I')
        self.grafo_1bf.adiciona_vertice('A')
        self.grafo_1bf.adiciona_vertice('B')
        self.grafo_1bf.adiciona_vertice('C')
        self.grafo_1bf.adiciona_vertice('D')
        self.grafo_1bf.adiciona_vertice('E')
        self.grafo_1bf.adiciona_aresta("a1", 'I', 'A', 10)
        self.grafo_1bf.adiciona_aresta("a2", 'I', 'E', 8)
        self.grafo_1bf.adiciona_aresta("a3", 'A', 'C', 2)
        self.grafo_1bf.adiciona_aresta("a4", 'B', 'A', 1)
        self.grafo_1bf.adiciona_aresta("a5", 'C', 'B', -2)
        self.grafo_1bf.adiciona_aresta("a6", 'D', 'C', -1)
        self.grafo_1bf.adiciona_aresta("a7", 'D', 'A', -4)
        self.grafo_1bf.adiciona_aresta("a8", 'E', 'D', 1)

        # Grafo somente com pesos positivos
        self.grafo_2bf = MeuGrafo()
        self.grafo_2bf.adiciona_vertice("V0")
        self.grafo_2bf.adiciona_vertice("V1")
        self.grafo_2bf.adiciona_vertice("V2")
        self.grafo_2bf.adiciona_vertice("V3")
        self.grafo_2bf.adiciona_vertice("V4")
        self.grafo_2bf.adiciona_vertice("V5")
        self.grafo_2bf.adiciona_aresta("a1", "V0", "V3", 3.5)
        self.grafo_2bf.adiciona_aresta("a2", "V0", "V2", 1.0)
        self.grafo_2bf.adiciona_aresta("a3", "V1", "V0", 6.0)
        self.grafo_2bf.adiciona_aresta("a4", "V1", "V4", 5.0)
        self.grafo_2bf.adiciona_aresta("a5", "V2", "V3", 2.0)
        self.grafo_2bf.adiciona_aresta("a6", "V2", "V4", 6.0)
        self.grafo_2bf.adiciona_aresta("a7", "V2", "V1", 2.5)
        self.grafo_2bf.adiciona_aresta("a8", "V3", "V5", 4.0)
        self.grafo_2bf.adiciona_aresta("a9", "V4", "V5", 3.0)
        self.grafo_2bf.adiciona_aresta("a10", "V5", "V2", 4.5)

        self.grafo_3bf = MeuGrafo()
        self.grafo_3bf.adiciona_vertice("S")
        self.grafo_3bf.adiciona_vertice("T")
        self.grafo_3bf.adiciona_vertice("X")
        self.grafo_3bf.adiciona_vertice("Y")
        self.grafo_3bf.adiciona_vertice("Z")
        self.grafo_3bf.adiciona_aresta("a1", "S", "T", 6)
        self.grafo_3bf.adiciona_aresta("a2", "S", "Y", 7)
        self.grafo_3bf.adiciona_aresta("a3", "T", "X", 5)
        self.grafo_3bf.adiciona_aresta("a4", "T", "Z", -4)
        self.grafo_3bf.adiciona_aresta("a5", "T", "Y", 8)
        self.grafo_3bf.adiciona_aresta("a6", "X", "T", -2)
        self.grafo_3bf.adiciona_aresta("a7", "Y", "X", -3)
        self.grafo_3bf.adiciona_aresta("a8", "Y", "Z", 9)
        self.grafo_3bf.adiciona_aresta("a9", "Z", "S", 2)
        self.grafo_3bf.adiciona_aresta("a10", "Z", "X", 7)

        # Grafo desconexo, mais de uma aresta e vertices
        self.grafo_4bf = MeuGrafo()
        self.grafo_4bf.adiciona_vertice('I')
        self.grafo_4bf.adiciona_vertice('A')
        self.grafo_4bf.adiciona_vertice('B')
        self.grafo_4bf.adiciona_vertice('C')
        self.grafo_4bf.adiciona_vertice('D')
        self.grafo_4bf.adiciona_vertice('E')
        self.grafo_4bf.adiciona_aresta("a1", 'I', 'A', 10)
        self.grafo_4bf.adiciona_aresta("a2", 'I', 'E', 8)
        self.grafo_4bf.adiciona_aresta("a3", 'A', 'C', 2)
        self.grafo_4bf.adiciona_aresta("a4", 'B', 'A', 1)
        self.grafo_4bf.adiciona_aresta("a5", 'C', 'B', -2)
        self.grafo_4bf.adiciona_aresta("a6", 'D', 'C', -1)
        self.grafo_4bf.adiciona_aresta("a7", 'D', 'A', -4)
        self.grafo_4bf.adiciona_aresta("a8", 'E', 'D', 1)
        self.grafo_4bf.adiciona_vertice('X')
        self.grafo_4bf.adiciona_vertice("Y")
        self.grafo_4bf.adiciona_vertice("Z")
        self.grafo_4bf.adiciona_vertice("W")
        self.grafo_4bf.adiciona_aresta("a9", "X", 'Y')
        self.grafo_4bf.adiciona_aresta("a10", "Z", 'Y')
        self.grafo_4bf.adiciona_aresta("a11", "Y", 'W')
        self.grafo_4bf.adiciona_aresta("a12", "Z", 'W')
        self.grafo_4bf.adiciona_aresta("a13", "W", 'Z')

        # Grafos com ciclos negativos
        self.grafo_5bf = MeuGrafo()
        self.grafo_5bf.adiciona_vertice("a")
        self.grafo_5bf.adiciona_vertice("b")
        self.grafo_5bf.adiciona_vertice("c")
        self.grafo_5bf.adiciona_aresta("a1", 'a', 'b', 4)
        self.grafo_5bf.adiciona_aresta("a2", 'b', 'c', -2)
        self.grafo_5bf.adiciona_aresta("a2", 'c', 'a', -3)


        self.grafo_6bf = MeuGrafo()
        self.grafo_6bf.adiciona_vertice("1")
        self.grafo_6bf.adiciona_vertice("2")
        self.grafo_6bf.adiciona_vertice("3")
        self.grafo_6bf.adiciona_vertice("4")
        self.grafo_6bf.adiciona_vertice("5")
        self.grafo_6bf.adiciona_vertice("6")
        self.grafo_6bf.adiciona_vertice("7")
        self.grafo_6bf.adiciona_vertice("8")
        self.grafo_6bf.adiciona_aresta("a1", "1", '2', 4)
        self.grafo_6bf.adiciona_aresta("a2", "1", '3', 4)
        self.grafo_6bf.adiciona_aresta("a3", "3", '6', -2)
        self.grafo_6bf.adiciona_aresta("a4", "3", '5', 4)
        self.grafo_6bf.adiciona_aresta("a5", "4", '3', 2)
        self.grafo_6bf.adiciona_aresta("a6", "4", '1', 3)
        self.grafo_6bf.adiciona_aresta("a7", "5", '4', 1)
        self.grafo_6bf.adiciona_aresta("a8", "5", '7', -2)
        self.grafo_6bf.adiciona_aresta("a9", "6", '2', 3)
        self.grafo_6bf.adiciona_aresta("a10", "6", '5', -3)
        self.grafo_6bf.adiciona_aresta("a11", "7", '6', 2)
        self.grafo_6bf.adiciona_aresta("a12", "7", '8', 2)
        self.grafo_6bf.adiciona_aresta("a13", "8", '5', -2)


        self.grafo_7bf = MeuGrafo()
        self.grafo_7bf.adiciona_vertice("0")
        self.grafo_7bf.adiciona_vertice("1")
        self.grafo_7bf.adiciona_vertice("2")
        self.grafo_7bf.adiciona_vertice("3")
        self.grafo_7bf.adiciona_aresta('a1', '1', '0', 4)
        self.grafo_7bf.adiciona_aresta('a2', '1', '2', -6)
        self.grafo_7bf.adiciona_aresta('a3', '2', '3', 5)
        self.grafo_7bf.adiciona_aresta('a4', '3', '1', -2)


    def test_adiciona_aresta(self):
        self.assertTrue(self.g_p.adiciona_aresta('a10', 'J', 'C'))
        a = ArestaDirecionada("zxc", self.g_p.get_vertice("C"), self.g_p.get_vertice("Z"))
        self.assertTrue(self.g_p.adiciona_aresta(a))
        with self.assertRaises(ArestaInvalidaError):
            self.assertTrue(self.g_p.adiciona_aresta(a))
        with self.assertRaises(VerticeInvalidoError):
            self.assertTrue(self.g_p.adiciona_aresta('b1', '', 'C'))
        with self.assertRaises(VerticeInvalidoError):
            self.assertTrue(self.g_p.adiciona_aresta('b1', 'A', 'C'))
        with self.assertRaises(TypeError):
            self.g_p.adiciona_aresta('')
        with self.assertRaises(TypeError):
            self.g_p.adiciona_aresta('aa-bb')
        with self.assertRaises(VerticeInvalidoError):
            self.g_p.adiciona_aresta('x', 'J', 'V')
        with self.assertRaises(ArestaInvalidaError):
            self.g_p.adiciona_aresta('a1', 'J', 'C')

    def test_remove_vertice(self):
        self.assertTrue(self.g_p.remove_vertice("J"))
        with self.assertRaises(VerticeInvalidoError):
            self.g_p.remove_vertice("J")
        with self.assertRaises(VerticeInvalidoError):
            self.g_p.remove_vertice("K")
        self.assertTrue(self.g_p.remove_vertice("C"))
        self.assertTrue(self.g_p.remove_vertice("Z"))

    def test_remove_aresta(self):
        self.assertTrue(self.g_p.remove_aresta("a1"))
        self.assertFalse(self.g_p.remove_aresta("a1"))
        self.assertTrue(self.g_p.remove_aresta("a7"))
        self.assertFalse(self.g_c.remove_aresta("a"))
        self.assertTrue(self.g_c.remove_aresta("a6"))
        self.assertTrue(self.g_c.remove_aresta("a1", "J"))
        self.assertTrue(self.g_c.remove_aresta("a5", "C"))
        with self.assertRaises(VerticeInvalidoError):
            self.g_p.remove_aresta("a2", "X", "C")
        with self.assertRaises(VerticeInvalidoError):
            self.g_p.remove_aresta("a3", "X")
        with self.assertRaises(VerticeInvalidoError):
            self.g_p.remove_aresta("a3", v2="X")

    def test_eq(self):
        self.assertEqual(self.g_p, self.g_p2)
        self.assertNotEqual(self.g_p, self.g_p3)
        self.assertNotEqual(self.g_p, self.g_p_sem_paralelas)
        self.assertNotEqual(self.g_p, self.g_p4)

    def test_vertices_nao_adjacentes(self):
        self.assertEqual(set(self.g_p.vertices_nao_adjacentes()), {'J-E', 'J-P', 'J-M', 'J-T', 'J-Z', 'C-J', 'C-T', 'C-Z', 'C-M', 'C-P', 'E-C', 'E-J', 'E-P',
                                                                   'E-M', 'E-T', 'E-Z', 'P-J', 'P-E', 'P-M', 'P-T', 'P-Z', 'M-J', 'M-E', 'M-P', 'M-Z', 'T-J',
                                                                   'T-M', 'T-E', 'T-P', 'Z-J', 'Z-C', 'Z-E', 'Z-P', 'Z-M', 'Z-T'})


        self.assertEqual(set(self.g_c.vertices_nao_adjacentes()), {'C-J', 'E-C', 'P-C', 'E-J', 'P-E', 'P-J'})
        self.assertEqual(self.g_c3.vertices_nao_adjacentes(), [])
        self.assertEqual(set(self.g_e.vertices_nao_adjacentes()), {'A-D', 'A-E', 'B-A', 'B-C', 'B-D', 'B-E', 'C-E', 'D-C', 'D-A', 'E-D', 'E-C'})

    def test_ha_laco(self):
        self.assertFalse(self.g_p.ha_laco())
        self.assertFalse(self.g_p_sem_paralelas.ha_laco())
        self.assertFalse(self.g_c2.ha_laco())
        self.assertTrue(self.g_l1.ha_laco())
        self.assertTrue(self.g_l2.ha_laco())
        self.assertTrue(self.g_l3.ha_laco())
        self.assertTrue(self.g_l4.ha_laco())
        self.assertTrue(self.g_l5.ha_laco())
        self.assertTrue(self.g_e.ha_laco())

    def test_grau(self):
        # Paraíba
        self.assertEqual(self.g_p.grau_saida('J'), 1)
        self.assertEqual(self.g_p.grau_entrada('J'), 0)
        self.assertEqual(self.g_p.grau_saida('C'), 2)
        self.assertEqual(self.g_p.grau_entrada('C'), 5)
        self.assertEqual(self.g_p.grau_saida('E'), 0)
        self.assertEqual(self.g_p.grau_entrada('E'), 2)
        self.assertEqual(self.g_p.grau_saida('P'), 2)
        self.assertEqual(self.g_p.grau_entrada('P'), 0)
        self.assertEqual(self.g_p.grau_saida('M'), 2)
        self.assertEqual(self.g_p.grau_entrada('M'), 0)
        self.assertEqual(self.g_p.grau_saida('T'), 2)
        self.assertEqual(self.g_p.grau_entrada('T'), 1)
        self.assertEqual(self.g_p.grau_saida('Z'), 0)
        self.assertEqual(self.g_p.grau_entrada('Z'), 1)
        with self.assertRaises(VerticeInvalidoError):
            self.assertEqual(self.g_p.grau_saida('G'), 5)

        self.assertEqual(self.g_d.grau_entrada('A'), 0)
        self.assertEqual(self.g_d.grau_saida('A'), 1)
        self.assertEqual(self.g_d.grau_entrada('C'), 0)
        self.assertEqual(self.g_d.grau_saida('C'), 0)
        self.assertNotEqual(self.g_d.grau_entrada('D'), 2)
        self.assertNotEqual(self.g_d.grau_entrada('D'), 2)
        self.assertEqual(self.g_d2.grau_entrada('A'), 0)
        self.assertNotEqual(self.g_d.grau_saida('D'), 2)

        # Completos
        self.assertEqual(self.g_c.grau_entrada('J'), 0)
        self.assertEqual(self.g_c.grau_saida('J'), 3)
        self.assertEqual(self.g_c.grau_entrada('C'), 1)
        self.assertEqual(self.g_c.grau_saida('C'), 2)
        self.assertEqual(self.g_c.grau_saida('E'), 1)
        self.assertEqual(self.g_c.grau_entrada('E'), 2)
        self.assertEqual(self.g_c.grau_saida('P'), 0)
        self.assertEqual(self.g_c.grau_entrada('P'), 3)

        # Com laço.
        self.assertEqual(self.g_l1.grau_saida('A'), 2)
        self.assertEqual(self.g_l1.grau_entrada('A'), 3)
        self.assertEqual(self.g_l2.grau_entrada('B'), 2)
        self.assertEqual(self.g_l2.grau_saida('B'), 2)
        self.assertEqual(self.g_l4.grau_entrada('D'), 1)
        self.assertEqual(self.g_l4.grau_saida('D'), 1)



    def test_ha_paralelas(self):
        self.assertTrue(self.g_p.ha_paralelas())
        self.assertFalse(self.g_p_sem_paralelas.ha_paralelas())
        self.assertFalse(self.g_c.ha_paralelas())
        self.assertFalse(self.g_c2.ha_paralelas())
        self.assertFalse(self.g_c3.ha_paralelas())
        self.assertTrue(self.g_l1.ha_paralelas())
        self.assertTrue(self.g_e.ha_paralelas())

    def test_arestas_sobre_vertice(self):
        self.assertEqual(set(self.g_p.arestas_sobre_vertice('J')), {'a1'})
        self.assertEqual(set(self.g_p.arestas_sobre_vertice('C')), {'a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7'})
        self.assertEqual(set(self.g_p.arestas_sobre_vertice('M')), {'a7', 'a8'})
        self.assertEqual(set(self.g_l2.arestas_sobre_vertice('B')), {'a1', 'a2', 'a3'})
        self.assertEqual(set(self.g_d.arestas_sobre_vertice('C')), set())
        self.assertEqual(set(self.g_d.arestas_sobre_vertice('A')), {'asd'})
        with self.assertRaises(VerticeInvalidoError):
            self.g_p.arestas_sobre_vertice('A')
        self.assertEqual(set(self.g_e.arestas_sobre_vertice('D')), {'5', '6', '7', '8'})


    def test_warshall(self):
        self.assertEqual(self.g_p_sem_paralelas.warshall(), self.g_p_sem_paralelas_matriz)
        self.assertEqual(self.g_p.warshall(), self.g_p_matriz)
        self.assertEqual(self.g_k4.warshall(), self.g_k4_matriz)
        self.assertEqual(self.g_c_c.warshall(), self.g_c_c_matriz)
        self.assertEqual(self.grafo_ap_l_1.warshall(), self.grafo_ap_l_1_matriz)
        self.assertEqual(self.g_e.warshall(), self.g_e_matriz)
        self.assertEqual(self.g_c_l_2.warshall(), self.g_c_l_2_matriz)
        self.assertEqual(self.g_l1.warshall(), self.g_l1_matriz)
        self.assertEqual(self.g_ap_l_2.warshall(), self.g_ap_l_2_matriz)
        self.assertEqual(self.g_ap_l_3.warshall(), self.g_ap_l_3_matriz)

    def test_dijkstra(self):
        self.assertEqual(self.grafo_1.dijkstra('A', 'E'), ['A', 'B', 'C', 'E'])
        self.assertEqual(self.grafo_2.dijkstra('A', 'E'), ['A', 'C', 'D', 'E'])
        self.assertEqual(self.grafo_3.dijkstra('A', 'F'), ['A', 'B', 'C', 'E', 'F'])
        self.assertEqual(self.grafo_2bf.dijkstra('E', 'B'), ['E', 'F', 'D', 'A', 'B'])
        self.assertEqual(self.grafo_5.dijkstra('1', '5'), ['1', '3', '6', '5'])
        self.assertEqual(self.grafo_6.dijkstra('0', '6'), ['0', '2', '7', '3', '6'])
        with self.assertRaises(VerticeInvalidoError):
            self.assertEqual(self.grafo_6.dijkstra('0', '8'), VerticeInvalidoError)
        with self.assertRaises(VerticeInvalidoError):
            self.assertEqual(self.grafo_3.dijkstra('G', 'C'), VerticeInvalidoError)
        with self.assertRaises(RuntimeError):
            self.assertEqual(self.grafo_7.dijkstra('A', 'T'), RuntimeError)
        with self.assertRaises(RuntimeError):
            self.assertEqual(self.grafo_1.dijkstra('C', 'B'), RuntimeError)

    def test_bellman_ford(self):

        # Grafo visto em aula
        self.assertEqual(self.grafo_1bf.bellman_ford("I", "C"), ['I', 'E', 'D', 'A', 'C'])
        # Grafo somente com pesos positivos
        self.assertEqual(self.grafo_2bf.bellman_ford('V0', 'V5'), ['V0', 'V2', 'V3', 'V5'])
        self.assertEqual(self.grafo_3bf.bellman_ford("S", "X"), ['S', 'Y', 'X'])
        # Testando vértices inexistentes
        with self.assertRaises(VerticeInvalidoError):
            self.assertEqual(self.grafo_3bf.bellman_ford("S", "W"))
            self.assertEqual(self.grafo_6bf.bellman_ford('A', 'B'))

        # Grafos desconexos
        self.assertFalse(self.grafo_4bf.bellman_ford("X", "A"))
        self.assertFalse(self.grafo_4bf.bellman_ford("C", "W"))
        self.assertEqual(self.grafo_4bf.bellman_ford("X", "W"), ['X', 'Y', 'W'])

        # Grafos com ciclos negativos
        self.assertFalse(self.grafo_5bf.bellman_ford('c', 'a'))
        self.assertFalse(self.grafo_6bf.bellman_ford('1', '8'))
        self.assertFalse(self.grafo_7bf.bellman_ford('1', '3'))


    def cria_matriz(self, grafo: MeuGrafo):
        ordem_matriz = len(grafo._vertices)
        nova_matriz = list()

        for i in range(ordem_matriz):
            nova_matriz.append(list())
            for j in range(ordem_matriz):
                nova_matriz[i].append(0)

        return nova_matriz





























