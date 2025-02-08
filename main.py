from traceback import print_tb

from bibgrafo import aresta
from bibgrafo.grafo_matriz_adj_dir import *
from bibgrafo.grafo_errors import *
from meu_grafo_matriz_adj_dir import MeuGrafo

# grafo_1 = MeuGrafo()
# grafo_1.adiciona_vertice('I')
# grafo_1.adiciona_vertice('A')
# grafo_1.adiciona_vertice('B')
# grafo_1.adiciona_vertice('C')
# grafo_1.adiciona_vertice('D')
# grafo_1.adiciona_vertice('E')
# #
# # grafo_1.adiciona_vertice('X')
# # grafo_1.adiciona_vertice("Y")
# # grafo_1.adiciona_vertice("Z")
# # grafo_1.adiciona_vertice("W")
# # grafo_1.adiciona_aresta("a9", "X", 'Y')
# # grafo_1.adiciona_aresta("a10", "Z", 'Y')
# # grafo_1.adiciona_aresta("a11", "Y", 'W')
# # grafo_1.adiciona_aresta("a12", "Z", 'W')
# # grafo_1.adiciona_aresta("a13", "W", 'Z')
# #
# grafo_1.adiciona_aresta("a1", 'I', 'A', 10)
# grafo_1.adiciona_aresta("a2", 'I', 'E', 8)
# grafo_1.adiciona_aresta("a3", 'A', 'C', 2)
# grafo_1.adiciona_aresta("a4", 'B', 'A', 1)
# grafo_1.adiciona_aresta("a5", 'C', 'B', -2)
# grafo_1.adiciona_aresta("a6", 'D', 'C', -1)
# grafo_1.adiciona_aresta("a7", 'D', 'A', -4)
# grafo_1.adiciona_aresta("a8", 'E', 'D', 1)
# #
#
#
# # Testando vertice inexistente
# # print(grafo_1.bellman_ford('I', 'T'))
#
# # Testando vertice existente e grafo desconexo
# # print(grafo_1.bellman_ford("I", "X"))
# # print(grafo_1.bellman_ford("X", "A"))
#
#
# grafo_2 = MeuGrafo()
# grafo_2.adiciona_vertice("A")
# grafo_2.adiciona_vertice("B")
# grafo_2.adiciona_vertice("C")
# grafo_2.adiciona_vertice("D")
# grafo_2.adiciona_vertice("E")
# grafo_2.adiciona_vertice("F")
# grafo_2.adiciona_aresta("a1", 'A', 'B', 9)
# grafo_2.adiciona_aresta("a2", 'A', 'C', 7)
# grafo_2.adiciona_aresta("a3", 'B', 'E', 2)
# grafo_2.adiciona_aresta("a4", 'C', 'D', 2)
# grafo_2.adiciona_aresta("a5", 'D', 'E', -2)
# grafo_2.adiciona_aresta("a6", 'D', 'B', -3)
# grafo_2.adiciona_aresta("a7", 'E', 'F', -2)
# grafo_2.adiciona_aresta("a8", 'F', 'B', 2)
#
#
# print(grafo_2.bellman_ford("A", "F"))
#
#
#
# selfgrafo_3bf = MeuGrafo()
# selfgrafo_3bf.adiciona_vertice("S")
# selfgrafo_3bf.adiciona_vertice("T")
# selfgrafo_3bf.adiciona_vertice("X")
# selfgrafo_3bf.adiciona_vertice("Y")
# selfgrafo_3bf.adiciona_vertice("Z")
# selfgrafo_3bf.adiciona_aresta("a1", "S", "T", 6)
# selfgrafo_3bf.adiciona_aresta("a2", "S", "Y", 7)
# selfgrafo_3bf.adiciona_aresta("a3", "T", "X", 5)
# selfgrafo_3bf.adiciona_aresta("a4", "T", "Z", -4)
# selfgrafo_3bf.adiciona_aresta("a5", "T", "Y", 8)
# selfgrafo_3bf.adiciona_aresta("a6", "X", "T", -2)
# selfgrafo_3bf.adiciona_aresta("a7", "Y", "X", -3)
# selfgrafo_3bf.adiciona_aresta("a8", "Y", "Z", 9)
# selfgrafo_3bf.adiciona_aresta("a9", "Z", "S", 2)
# selfgrafo_3bf.adiciona_aresta("a10", "Z", "X", 7)
#
# print(selfgrafo_3bf.bellman_ford('S', 'Y'))
#
#
#
# # grafo_4 = MeuGrafo()
# # grafo_4.adiciona_vertice("V0")
# # grafo_4.adiciona_vertice("V1")
# # grafo_4.adiciona_vertice("V2")
# # grafo_4.adiciona_vertice("V3")
# # grafo_4.adiciona_vertice("V4")
# # grafo_4.adiciona_vertice("V5")
# # grafo_4.adiciona_aresta("a1", "V0", "V3", 3.5)
# # grafo_4.adiciona_aresta("a2", "V0", "V2", 1.0)
# # grafo_4.adiciona_aresta("a3", "V1", "V0", 6.0)
# # grafo_4.adiciona_aresta("a4", "V1", "V4", 5.0)
# # grafo_4.adiciona_aresta("a5", "V2", "V3", 2.0)
# # grafo_4.adiciona_aresta("a6", "V2", "V4", 6.0)
# # grafo_4.adiciona_aresta("a7", "V2", "V1", 2.5)
# # grafo_4.adiciona_aresta("a8", "V3", "V5", 4.0)
# # grafo_4.adiciona_aresta("a9", "V4", "V5", 3.0)
# # grafo_4.adiciona_aresta("a10", "V5", "V2", 4.5)
# #
# # print(grafo_4.bellman_ford("V0", "V5"))
#
#
#
#
#
#
#
#
#
#
# grafo_5 = MeuGrafo()
# grafo_5.adiciona_vertice("A")
# grafo_5.adiciona_vertice("B")
# grafo_5.adiciona_vertice("C")
# grafo_5.adiciona_vertice("D")
# grafo_5.adiciona_vertice("E")
# grafo_5.adiciona_vertice("F")
# grafo_5.adiciona_aresta("a1", 'A', 'B', 5)
# grafo_5.adiciona_aresta("a2", 'A', 'C', -2)
# grafo_5.adiciona_aresta("a3", 'B', 'D', 1)
# grafo_5.adiciona_aresta("a4", 'C', 'B', 2)
# grafo_5.adiciona_aresta("a5", 'C', 'E', 3)
# grafo_5.adiciona_aresta("a6", 'D', 'C', 2)
# grafo_5.adiciona_aresta("a7", 'D', 'E', 7)
# grafo_5.adiciona_aresta("a8", 'D', 'F', 3)
# grafo_5.adiciona_aresta("a9", 'E', 'F', 10)
# # --
# #grafo_5.adiciona_aresta("a10", 'E', 'B', -4)
# print(grafo_5.bellman_ford("A", "E"))
#
# grafo_6 = MeuGrafo()
# grafo_6.adiciona_vertice("a")
# grafo_6.adiciona_vertice("b")
# grafo_6.adiciona_vertice("c")
# grafo_6.adiciona_vertice("d")
# grafo_6.adiciona_vertice("e")
# grafo_6.adiciona_vertice("f")
# grafo_6.adiciona_aresta("a1", 'a', 'b', 9)
# grafo_6.adiciona_aresta("a2", 'a', 'c', 7)
# grafo_6.adiciona_aresta("a3", 'b', 'e', 3)
# grafo_6.adiciona_aresta("a4", 'b', 'f', -1)
# grafo_6.adiciona_aresta("a5", 'b', 'd', 1)
# grafo_6.adiciona_aresta("a6", 'c', 'b', -2)
# grafo_6.adiciona_aresta("a7", 'c', 'd', 2)
# grafo_6.adiciona_aresta("a8", 'd', 'f', 1)
# grafo_6.adiciona_aresta("a9", 'f', 'e', 1)
#
#
# print(grafo_6.bellman_ford("a", "f"))


# grafo com ciclo negativo

grafo_7 = MeuGrafo()
grafo_7.adiciona_vertice("a")
grafo_7.adiciona_vertice("b")
grafo_7.adiciona_vertice("c")
grafo_7.adiciona_aresta("a1", 'a','b', 4)
grafo_7.adiciona_aresta("a2", 'b', 'c', -2)
grafo_7.adiciona_aresta("a2", 'c', 'a', -3)

print(grafo_7.bellman_ford("c", "a"))




















































































