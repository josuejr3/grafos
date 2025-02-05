import unittest
from meu_grafo_lista_adj_nao_dir import *
import gerar_grafos_teste
from bibgrafo.aresta import Aresta
from bibgrafo.vertice import Vertice
from bibgrafo.grafo_errors import *
from bibgrafo.grafo_json import GrafoJSON
from bibgrafo.grafo_builder import GrafoBuilder


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
        self.g_p_sem_paralelas = MeuGrafo()
        self.g_p_sem_paralelas.adiciona_vertice("J")
        self.g_p_sem_paralelas.adiciona_vertice("C")
        self.g_p_sem_paralelas.adiciona_vertice("E")
        self.g_p_sem_paralelas.adiciona_vertice("P")
        self.g_p_sem_paralelas.adiciona_vertice("M")
        self.g_p_sem_paralelas.adiciona_vertice("T")
        self.g_p_sem_paralelas.adiciona_vertice("Z")
        self.g_p_sem_paralelas.adiciona_aresta('a1', 'J', 'C')
        self.g_p_sem_paralelas.adiciona_aresta('a2', 'C', 'E')
        self.g_p_sem_paralelas.adiciona_aresta('a3', 'P', 'C')
        self.g_p_sem_paralelas.adiciona_aresta('a4', 'T', 'C')
        self.g_p_sem_paralelas.adiciona_aresta('a5', 'M', 'C')
        self.g_p_sem_paralelas.adiciona_aresta('a6', 'M', 'T')
        self.g_p_sem_paralelas.adiciona_aresta('a7', 'T', 'Z')

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

        self.g_l4 = GrafoBuilder().tipo(MeuGrafo()).vertices([v:=Vertice('D')]) \
            .arestas([Aresta('a1', v, v)]).build()

        self.g_l5 = GrafoBuilder().tipo(MeuGrafo()).vertices(3) \
            .arestas(3, lacos=1).build()

        # Grafos desconexos
        self.g_d = GrafoBuilder().tipo(MeuGrafo()) \
            .vertices([a:=Vertice('A'), b:=Vertice('B'), Vertice('C'), Vertice('D')]) \
            .arestas([Aresta('asd', a, b)]).build()

        self.g_d2 = GrafoBuilder().tipo(MeuGrafo()).vertices(4).build()

        # Grafo p\teste de remoção em casta
        self.g_r = GrafoBuilder().tipo(MeuGrafo()).vertices(2).arestas(1).build()


        # 1 - COMPLETO K1 - Um vértice
        self.g_unico = MeuGrafo()
        self.g_unico.adiciona_vertice("Único")

        # 2 - GRAFO COM UMA ARESTA (K2)
        self.gr_k2 = MeuGrafo()
        self.gr_k2.adiciona_vertice("1")
        self.gr_k2.adiciona_vertice("2")
        self.gr_k2.adiciona_aresta("edge", "1", "2")

        # 3 - Grafo K3
        self.g_k3 = MeuGrafo()
        self.g_k3.adiciona_vertice("1")
        self.g_k3.adiciona_vertice("2")
        self.g_k3.adiciona_vertice("3")
        self.g_k3.adiciona_aresta("a1", "1", "2")
        self.g_k3.adiciona_aresta("a2", "2", "3")
        self.g_k3.adiciona_aresta("a3", "3", "1")

        # 3 - Resposta K3
        self.g_k3_with_bfs = MeuGrafo()
        self.g_k3_with_bfs.adiciona_vertice("1")
        self.g_k3_with_bfs.adiciona_vertice("2")
        self.g_k3_with_bfs.adiciona_vertice("3")
        self.g_k3_with_bfs.adiciona_aresta("a1", "1", "2")
        self.g_k3_with_bfs.adiciona_aresta("a3", "3", "1")

        # 3 - Grafo simples conexo
        self.g_teste3 = MeuGrafo()
        self.g_teste3.adiciona_vertice("A")
        self.g_teste3.adiciona_vertice("B")
        self.g_teste3.adiciona_vertice("C")
        self.g_teste3.adiciona_vertice("D")
        self.g_teste3.adiciona_aresta("a1", "A", "B")
        self.g_teste3.adiciona_aresta("a2", "B", "D")
        self.g_teste3.adiciona_aresta("a3", "B", "C")

        # 4 - Grafo Paraíba
        self.g_paraiba = MeuGrafo()
        self.g_paraiba.adiciona_vertice("J")
        self.g_paraiba.adiciona_vertice("C")
        self.g_paraiba.adiciona_vertice("E")
        self.g_paraiba.adiciona_vertice("P")
        self.g_paraiba.adiciona_vertice("M")
        self.g_paraiba.adiciona_vertice("T")
        self.g_paraiba.adiciona_vertice("Z")
        self.g_paraiba.adiciona_aresta("a1", "J", "C")
        self.g_paraiba.adiciona_aresta("a2", "C", "E")
        self.g_paraiba.adiciona_aresta("a3", "C", "E")
        self.g_paraiba.adiciona_aresta("a4", "P", "C")
        self.g_paraiba.adiciona_aresta("a5", "P", "C")
        self.g_paraiba.adiciona_aresta("a6", "T", "C")
        self.g_paraiba.adiciona_aresta("a7", "M", "C")
        self.g_paraiba.adiciona_aresta("a8", "M", "T")
        self.g_paraiba.adiciona_aresta("a9", "T", "Z")

        # 4 - Grafo Paraiba começando em J
        self.g_paraiba_with_dfs = MeuGrafo()
        self.g_paraiba_with_dfs.adiciona_vertice("J")
        self.g_paraiba_with_dfs.adiciona_vertice("C")
        self.g_paraiba_with_dfs.adiciona_vertice("E")
        self.g_paraiba_with_dfs.adiciona_vertice("P")
        self.g_paraiba_with_dfs.adiciona_vertice("M")
        self.g_paraiba_with_dfs.adiciona_vertice("T")
        self.g_paraiba_with_dfs.adiciona_vertice("Z")
        self.g_paraiba_with_dfs.adiciona_aresta("a1", "J", "C")
        self.g_paraiba_with_dfs.adiciona_aresta("a2", "C", "E")
        self.g_paraiba_with_dfs.adiciona_aresta("a4", "C", "P")
        self.g_paraiba_with_dfs.adiciona_aresta("a6", "C", "T")
        self.g_paraiba_with_dfs.adiciona_aresta("a8", "M", "T")
        self.g_paraiba_with_dfs.adiciona_aresta("a9", "T", "Z")

        # 5 - Grafo áciclico
        self.g_aciclico = MeuGrafo()
        self.g_aciclico.adiciona_vertice("P")
        self.g_aciclico.adiciona_vertice("S")
        self.g_aciclico.adiciona_vertice("T")
        self.g_aciclico.adiciona_vertice("Q")
        self.g_aciclico.adiciona_aresta("a1", "P", "S")
        self.g_aciclico.adiciona_aresta("a2", "S", "T")
        self.g_aciclico.adiciona_aresta("a3", "T", "Q")

        # 6 - Grafo com laço
        self.g_cl = MeuGrafo()
        self.g_cl.adiciona_vertice("P1")
        self.g_cl.adiciona_vertice("P2")
        self.g_cl.adiciona_vertice("P3")
        self.g_cl.adiciona_vertice("P4")
        self.g_cl.adiciona_aresta("a1", "P1", "P2")
        self.g_cl.adiciona_aresta("a2", "P2", "P3")
        self.g_cl.adiciona_aresta("a3", "P3", "P4")
        self.g_cl.adiciona_aresta("a4", "P4", "P1")
        self.g_cl.adiciona_aresta("a5", "P2", "P2")
        self.g_cl.adiciona_aresta("a6", "P4", "P4")

        # 6 - Resposta Grafo com laço começando de P3
        self.g_cl_with_dfs = MeuGrafo()
        self.g_cl_with_dfs.adiciona_vertice("P1")
        self.g_cl_with_dfs.adiciona_vertice("P2")
        self.g_cl_with_dfs.adiciona_vertice("P3")
        self.g_cl_with_dfs.adiciona_vertice("P4")
        self.g_cl_with_dfs.adiciona_aresta("a2", "P2", "P3")
        self.g_cl_with_dfs.adiciona_aresta("a1", "P1", "P2")
        self.g_cl_with_dfs.adiciona_aresta("a4", "P4", "P1")

        # 7 - Outro grafo com laço
        self.g_cl2 = MeuGrafo()
        self.g_cl2.adiciona_vertice("A")
        self.g_cl2.adiciona_vertice("B")
        self.g_cl2.adiciona_vertice("C")
        self.g_cl2.adiciona_aresta("a1", "A", "A")
        self.g_cl2.adiciona_aresta("a2", "A", "B")
        self.g_cl2.adiciona_aresta("a3", "B", "C")
        self.g_cl2.adiciona_aresta("a4", "C", "C")

        # 7 - Resposta começando em C
        self.g_cl2_with_dfs = MeuGrafo()
        self.g_cl2_with_dfs.adiciona_vertice("A")
        self.g_cl2_with_dfs.adiciona_vertice("B")
        self.g_cl2_with_dfs.adiciona_vertice("C")
        self.g_cl2_with_dfs.adiciona_aresta("a2", "A", "B")
        self.g_cl2_with_dfs.adiciona_aresta("a3", "B", "C")

        # 8 - Grafo com laço e desconexo
        self.g_cl3 = MeuGrafo()
        self.g_cl3.adiciona_vertice("1")
        self.g_cl3.adiciona_vertice("2")
        self.g_cl3.adiciona_vertice("3")
        self.g_cl3.adiciona_aresta("a1", "1", "1")
        self.g_cl3.adiciona_aresta("a2", "2", "2")
        self.g_cl3.adiciona_aresta("a3", "3", "3")

        # 9 - Grafo desconexo
        self.g_desconexo = MeuGrafo()
        self.g_desconexo.adiciona_vertice("A")
        self.g_desconexo.adiciona_vertice("B")
        self.g_desconexo.adiciona_vertice("C")
        self.g_desconexo.adiciona_vertice("D")
        self.g_desconexo.adiciona_vertice("E")
        self.g_desconexo.adiciona_vertice("F")
        self.g_desconexo.adiciona_aresta("a1", "A", "C")
        self.g_desconexo.adiciona_aresta("a2", "B", "C")
        self.g_desconexo.adiciona_aresta("a3", "E", "D")
        self.g_desconexo.adiciona_aresta("a4", "F", "D")

        # 10 - Grafo arestas paralelas
        self.g_ap = MeuGrafo()
        self.g_ap.adiciona_vertice("1")
        self.g_ap.adiciona_vertice("2")
        self.g_ap.adiciona_vertice("3")
        self.g_ap.adiciona_aresta("a1", "1", "2")
        self.g_ap.adiciona_aresta("a2", "1", "2")
        self.g_ap.adiciona_aresta("a3", "2", "3")

        # Começando de 2
        self.g_ap_with_dfs = MeuGrafo()
        self.g_ap_with_dfs.adiciona_vertice("1")
        self.g_ap_with_dfs.adiciona_vertice("2")
        self.g_ap_with_dfs.adiciona_vertice("3")
        self.g_ap_with_dfs.adiciona_aresta("a3", "2", "3")
        self.g_ap_with_dfs.adiciona_aresta("a1", "1", "2")

        # Grafo Paraíba BFS começando em M
        self.g_paraiba_with_bfs = MeuGrafo()
        self.g_paraiba_with_bfs.adiciona_vertice("J")
        self.g_paraiba_with_bfs.adiciona_vertice("C")
        self.g_paraiba_with_bfs.adiciona_vertice("E")
        self.g_paraiba_with_bfs.adiciona_vertice("P")
        self.g_paraiba_with_bfs.adiciona_vertice("M")
        self.g_paraiba_with_bfs.adiciona_vertice("T")
        self.g_paraiba_with_bfs.adiciona_vertice("Z")
        self.g_paraiba_with_bfs.adiciona_aresta("a1", "J", "C")
        self.g_paraiba_with_bfs.adiciona_aresta("a2", "C", "E")
        self.g_paraiba_with_bfs.adiciona_aresta("a4", "P", "C")
        self.g_paraiba_with_bfs.adiciona_aresta("a7", "M", "C")
        self.g_paraiba_with_bfs.adiciona_aresta("a8", "M", "T")
        self.g_paraiba_with_bfs.adiciona_aresta("a9", "T", "Z")

        # Grafo Paraiba BFS começando em T
        self.g_paraiba_with_bfs_t = MeuGrafo()
        self.g_paraiba_with_bfs_t.adiciona_vertice("J")
        self.g_paraiba_with_bfs_t.adiciona_vertice("C")
        self.g_paraiba_with_bfs_t.adiciona_vertice("E")
        self.g_paraiba_with_bfs_t.adiciona_vertice("P")
        self.g_paraiba_with_bfs_t.adiciona_vertice("M")
        self.g_paraiba_with_bfs_t.adiciona_vertice("T")
        self.g_paraiba_with_bfs_t.adiciona_vertice("Z")
        self.g_paraiba_with_bfs_t.adiciona_aresta("a1", "J", "C")
        self.g_paraiba_with_bfs_t.adiciona_aresta("a2", "C", "E")
        self.g_paraiba_with_bfs_t.adiciona_aresta("a4", "P", "C")
        self.g_paraiba_with_bfs_t.adiciona_aresta("a6", "C", "T")
        self.g_paraiba_with_bfs_t.adiciona_aresta("a8", "M", "T")
        self.g_paraiba_with_bfs_t.adiciona_aresta("a9", "T", "Z")

        self.g_vertice_isolado = MeuGrafo()
        self.g_vertice_isolado.adiciona_vertice("A")
        self.g_vertice_isolado.adiciona_vertice("B")
        self.g_vertice_isolado.adiciona_vertice("C")
        self.g_vertice_isolado.adiciona_vertice("D")
        self.g_vertice_isolado.adiciona_aresta("a1", "B", "C")
        self.g_vertice_isolado.adiciona_aresta("a2", "C", "D")
        self.g_vertice_isolado.adiciona_aresta("a3", "D", "B")
        self.g_vertice_isolado.adiciona_aresta("a4", "A", "A")

        self.g_desconexo2 = MeuGrafo()
        self.g_desconexo2.adiciona_vertice("A")
        self.g_desconexo2.adiciona_vertice("B")
        self.g_desconexo2.adiciona_vertice("C")
        self.g_desconexo2.adiciona_vertice("D")
        self.g_desconexo2.adiciona_aresta("Unica", "C", "D")


    def test_adiciona_aresta(self):
        self.assertTrue(self.g_p.adiciona_aresta('a10', 'J', 'C'))
        a = Aresta("zxc", self.g_p.get_vertice("C"), self.g_p.get_vertice("Z"))
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
        self.assertIsNone(self.g_r.remove_vertice('A'))
        self.assertFalse(self.g_r.existe_rotulo_vertice('A'))
        self.assertFalse(self.g_r.existe_rotulo_aresta('1'))
        with self.assertRaises(VerticeInvalidoError):
            self.g_r.get_vertice('A')
        self.assertFalse(self.g_r.get_aresta('1'))
        self.assertEqual(self.g_r.arestas_sobre_vertice('B'), set())

    def test_eq(self):
        self.assertEqual(self.g_p, self.g_p2)
        self.assertNotEqual(self.g_p, self.g_p3)
        self.assertNotEqual(self.g_p, self.g_p_sem_paralelas)
        self.assertNotEqual(self.g_p, self.g_p4)

    def test_vertices_nao_adjacentes(self):
        self.assertEqual(self.g_p.vertices_nao_adjacentes(),
                         {'J-E', 'J-P', 'J-M', 'J-T', 'J-Z', 'C-Z', 'E-P', 'E-M', 'E-T', 'E-Z', 'P-M', 'P-T', 'P-Z',
                          'M-Z'})
        self.assertEqual(self.g_d.vertices_nao_adjacentes(), {'A-C', 'A-D', 'B-C', 'B-D', 'C-D'})
        self.assertEqual(self.g_d2.vertices_nao_adjacentes(), {'A-B', 'A-C', 'A-D', 'B-C', 'B-D', 'C-D'})
        self.assertEqual(self.g_c.vertices_nao_adjacentes(), set())
        self.assertEqual(self.g_c3.vertices_nao_adjacentes(), set())

    def test_ha_laco(self):
        self.assertFalse(self.g_p.ha_laco())
        self.assertFalse(self.g_p2.ha_laco())
        self.assertFalse(self.g_p3.ha_laco())
        self.assertFalse(self.g_p4.ha_laco())
        self.assertFalse(self.g_p_sem_paralelas.ha_laco())
        self.assertFalse(self.g_d.ha_laco())
        self.assertFalse(self.g_c.ha_laco())
        self.assertFalse(self.g_c2.ha_laco())
        self.assertFalse(self.g_c3.ha_laco())
        self.assertTrue(self.g_l1.ha_laco())
        self.assertTrue(self.g_l2.ha_laco())
        self.assertTrue(self.g_l3.ha_laco())
        self.assertTrue(self.g_l4.ha_laco())
        self.assertTrue(self.g_l5.ha_laco())

    def test_grau(self):
        # Paraíba
        self.assertEqual(self.g_p.grau('J'), 1)
        self.assertEqual(self.g_p.grau('C'), 7)
        self.assertEqual(self.g_p.grau('E'), 2)
        self.assertEqual(self.g_p.grau('P'), 2)
        self.assertEqual(self.g_p.grau('M'), 2)
        self.assertEqual(self.g_p.grau('T'), 3)
        self.assertEqual(self.g_p.grau('Z'), 1)
        with self.assertRaises(VerticeInvalidoError):
            self.assertEqual(self.g_p.grau('G'), 5)

        self.assertEqual(self.g_d.grau('A'), 1)
        self.assertEqual(self.g_d.grau('C'), 0)
        self.assertNotEqual(self.g_d.grau('D'), 2)
        self.assertEqual(self.g_d2.grau('A'), 0)

        # Completos
        self.assertEqual(self.g_c.grau('J'), 3)
        self.assertEqual(self.g_c.grau('C'), 3)
        self.assertEqual(self.g_c.grau('E'), 3)
        self.assertEqual(self.g_c.grau('P'), 3)

        # Com laço. Lembrando que cada laço conta 2 vezes por vértice para cálculo do grau
        self.assertEqual(self.g_l1.grau('A'), 5)
        self.assertEqual(self.g_l2.grau('B'), 4)
        self.assertEqual(self.g_l4.grau('D'), 2)

    def test_ha_paralelas(self):
        self.assertTrue(self.g_p.ha_paralelas())
        self.assertFalse(self.g_p_sem_paralelas.ha_paralelas())
        self.assertFalse(self.g_c.ha_paralelas())
        self.assertFalse(self.g_c2.ha_paralelas())
        self.assertFalse(self.g_c3.ha_paralelas())
        self.assertTrue(self.g_l1.ha_paralelas())

    def test_arestas_sobre_vertice(self):
        self.assertEqual(self.g_p.arestas_sobre_vertice('J'), {'a1'})
        self.assertEqual(self.g_p.arestas_sobre_vertice('C'), {'a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7'})
        self.assertEqual(self.g_p.arestas_sobre_vertice('M'), {'a7', 'a8'})
        self.assertEqual(self.g_l2.arestas_sobre_vertice('B'), {'a1', 'a2', 'a3'})
        self.assertEqual(self.g_d.arestas_sobre_vertice('C'), set())
        self.assertEqual(self.g_d.arestas_sobre_vertice('A'), {'asd'})
        with self.assertRaises(VerticeInvalidoError):
            self.g_p.arestas_sobre_vertice('A')

    def test_eh_completo(self):
        self.assertFalse(self.g_p.eh_completo())
        self.assertFalse((self.g_p_sem_paralelas.eh_completo()))
        self.assertTrue((self.g_c.eh_completo()))
        self.assertTrue((self.g_c2.eh_completo()))
        self.assertTrue((self.g_c3.eh_completo()))
        self.assertFalse((self.g_l1.eh_completo()))
        self.assertFalse((self.g_l2.eh_completo()))
        self.assertFalse((self.g_l3.eh_completo()))
        self.assertFalse((self.g_l4.eh_completo()))
        self.assertFalse((self.g_l5.eh_completo()))
        self.assertFalse((self.g_d.eh_completo()))
        self.assertFalse((self.g_d2.eh_completo()))

    def test_dfs(self):

        # Grafo Simples
        self.assertEqual(self.g_teste3.dfs("B"), self.g_teste3)

        # Grafo K2
        self.assertEqual(self.gr_k2.dfs("2"), self.gr_k2)

        # Grafo de um único vértice
        #self.assertEqual(self.g_c3.dfs("Único"), self.g_c3)

        # Grafos da Paraíba
        self.assertEqual(self.g_paraiba.dfs("J"), self.g_paraiba_with_dfs)

        # Grafo com laços
        self.assertEqual(self.g_cl.dfs("P3"), self.g_cl_with_dfs)
        self.assertEqual(self.g_cl2.dfs("C"), self.g_cl2_with_dfs)
        self.assertFalse(self.g_cl3.dfs("3"))

        # Grafos desconexos
        self.assertFalse(self.g_desconexo.dfs("D"))
        self.assertFalse(self.g_desconexo.dfs("C"))
        self.assertFalse(self.g_desconexo.dfs("A"))

        # Grafo arestas paralelas
        self.assertEqual(self.g_ap.dfs("2"), self.g_ap_with_dfs)

        # Vértices inexistentes
        with self.assertRaises(VerticeInvalidoError):
            self.g_paraiba.dfs("B")
            self.g_aciclico.dfs("X")

    def test_bfs(self):

        # Grafo de um único vértice
        self.assertEqual(self.g_unico.bfs("Único"), self.g_unico)

        # Grafo Simples
        self.assertEqual(self.g_teste3.bfs("B"), self.g_teste3)

        # Grafo K3
        self.assertEqual(self.g_k3.bfs("1"), self.g_k3_with_bfs)

        # Grafo K2
        self.assertEqual(self.gr_k2.bfs("2"), self.gr_k2)

        # Grafo da Paraíba
        self.assertEqual(self.g_paraiba.bfs("M"), self.g_paraiba_with_bfs)
        self.assertEqual(self.g_paraiba.bfs("T"), self.g_paraiba_with_bfs_t)

        # Vértices inexistentes
        with self.assertRaises(VerticeInvalidoError):
            self.g_paraiba.bfs("B")
            self.g_aciclico.bfs("X")

        # Grafo desconexo
        self.assertFalse(self.g_desconexo.bfs("D"))
        self.assertFalse(self.g_desconexo.bfs("C"))
        self.assertFalse(self.g_desconexo.bfs("A"))

    def test_caminho(self):

        # Grafo de um único vértice e passando o tamanho do caminho como menor ou igual a 0
        self.assertFalse(self.g_unico.caminho(1))
        self.assertFalse(self.g_paraiba.caminho(-15))
        self.assertFalse(self.g_unico.caminho(0))

        # Grafo simples
        self.assertEqual(self.g_teste3.caminho(1), ["A", "a1", "B"])

        # Grafo aciclio
        self.assertEqual(self.g_aciclico.caminho(2), ["P", "a1", "S", "a2", "T"])

        # Grafo da paraíba
        self.assertEqual(self.g_paraiba.caminho(3), ["J", "a1", "C", "a6", "T", "a8", "M"])
        self.assertEqual(self.g_paraiba.caminho(2), ["J", "a1", "C", "a2", "E"])
        self.assertEqual(self.g_paraiba.caminho(1), ["J", "a1", "C"])

        # Grafo Paraiba sem arestas paralelas.
        self.assertEqual(self.g_p_sem_paralelas.caminho(4), ["J", "a1", "C", "a5", "M", "a6", "T", "a7", "Z"])
        self.assertEqual(self.g_ap.caminho(2), ["1", "a1", "2", "a3", "3"])

        # Grafo desconexo
        self.assertFalse(self.g_desconexo.caminho(3))
        self.assertEqual(self.g_desconexo.caminho(2), ["A", "a1", "C", "a2", "B"])
        self.assertEqual(self.g_vertice_isolado.caminho(3), False)

        # Grafo com primeiros vértices desconectados do restante
        self.assertEqual(self.g_desconexo2.caminho(1), ["C", "Unica", "D"])
        self.assertFalse(self.g_desconexo2.caminho(5))

        # Grafo com laço
        self.assertFalse(self.g_cl3.caminho(3))
        self.assertEqual(self.g_cl2.caminho(2), ["A", "a2", "B", "a3", "C"])
        self.assertEqual(self.g_cl.caminho(3), ["P1", "a1", "P2", "a2", "P3", "a3", "P4"])
        self.assertFalse(self.g_cl.caminho(4))

    def test_conexo(self):

        # Único vértice, k2 e k3
        self.assertFalse(self.g_unico.conexo())
        self.assertTrue(self.g_k3.conexo())
        self.assertTrue(self.gr_k2.conexo())

        # Grafo da Paraíba
        self.assertTrue(self.g_paraiba.conexo())
        self.assertTrue(self.g_p_sem_paralelas.conexo())

        # Grafos desconexos
        self.assertFalse(self.g_desconexo.conexo())
        self.assertFalse(self.g_desconexo2.conexo())
        self.assertFalse(self.g_vertice_isolado.conexo())

        # Grafos com laços
        self.assertTrue(self.g_cl.conexo())
        self.assertTrue(self.g_cl2.conexo())
        self.assertFalse(self.g_cl3.conexo())

        # Grafo aciclico
        self.assertTrue(self.g_aciclico.conexo())
        # Grafo com arestas paralelas
        self.assertTrue(self.g_ap.conexo())

    def test_ha_ciclo(self):

        # Grafo com nenhuma aresta e um vértice
        self.assertFalse(self.g_unico.ha_ciclo())

        # Grafo K2 e K3
        self.assertFalse(self.gr_k2.ha_ciclo())
        self.assertEqual(self.g_k3.ha_ciclo(), ["1", "a1", "2", "a2", "3", "a3", "1"])

        # Grafo simples conexo
        self.assertFalse(self.g_teste3.ha_ciclo())

        # Grafo Paraíba
        self.assertEqual(self.g_paraiba.ha_ciclo(), ["C", "a2", "E", "a3", "C"])
        # Grafo da Paraíba sem arestas paralelas
        self.assertEqual(self.g_p_sem_paralelas.ha_ciclo(), ["C", "a4", "T", "a6", "M", "a5", "C"])

        # Grafo aciclico
        self.assertFalse(self.g_aciclico.ha_ciclo())

        # Grafos com laço
        self.assertEqual(self.g_cl.ha_ciclo(), ["P1", "a1", "P2", "a2", "P3", "a3", "P4", "a4", "P1"])
        self.assertFalse(self.g_cl2.ha_ciclo())
        self.assertFalse(self.g_cl3.ha_ciclo())
        self.assertEqual(self.g_vertice_isolado.ha_ciclo(), ["B", "a1", "C", "a2", "D", "a3", "B"])

        # Grafo desconexo
        self.assertFalse(self.g_desconexo.ha_ciclo())
        self.assertFalse(self.g_desconexo2.ha_ciclo())

        # Grafo com arestas paralelas
        self.assertEqual(self.g_ap.ha_ciclo(), ["1", "a1", "2", "a2", "1"])









