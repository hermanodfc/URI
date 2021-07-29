class No:

    def __init__(self, key):
        self.parent = None
        self.altura = 0
        self.left = None
        self.right = None
        self.key = key

class ArvoreAVL:

    def __init__(self):
        self.root = None

    def search(self, no, key):

        count = 1
        while no is not None and key != no.key:
            count += 1
            if self.menor(key, no.key):
                no = no.left
            else:
                no = no.right

        if no is None:
            return None,

        return no

    def search_ge(self, key):

        parent = None
        son = self.root

        while son is not None:
            parent = son
            if key < son.key:
                son = son.left
            elif key > son.key:
                son = son.right
            else:
                return son


        if parent is None:
            return None

        if parent.key > key:
            return parent

        return self.sucessor(parent)


    def minimum(self, no):

        if no is not None:
            while no.left is not None:
                no = no.left

        return no

    def maximum(self, no):

        if no is not None:
            while no.right is not None:
                no = no.right

        return no

    def sucessor(self, no):

        if no is not None:
            if no.right is not None:
                return self.minimum(no.right)

            parent = no.parent

            while parent is not None and no == parent.right:
                no = parent
                parent = parent.parent

            return parent

    def predecessor(self, no):

        if no is not None:
            if no.left is not None:
                return self.maximum(no.left)

            parent = no.parent

            while parent is not None and no == parent.left:
                no = parent
                parent = parent.parent

            return parent

    def inserir(self, key):

        no = No(key)

        parent = None
        son = self.root

        while son is not None and key != son.key:
            parent = son
            if self.menor(key, son.key):
                son = son.left
            else:
                son = son.right

        no.parent = parent

        if parent is None:
            self.root = no
        elif self.menor(key, parent.key):
            parent.left = no
        else:
            parent.right = no

        self.rebalance(no)

    def rebalance(self, no):

        while no is not self.root:
            no = no.parent

            if abs(self.rank(no)) > 1:
                no = self.rotacionar(no)

            no.altura = self.altura(no)

    def rotacionar(self, no):
        rank_no = self.rank(no)

        if no.left is None:
            y = no.right
        elif no.right is None:
            y = no.left
        elif no.right.altura > no.left.altura:
            y = no.right
        else:
            y = no.left

        rank_y = self.rank(y)

        if rank_no > 0:
            if rank_y < 0:
                self.right_rotate(y)
            return self.left_rotate(no)
        else: #rank_no <= 0
            if rank_y > 0:
                self.left_rotate(y)
            return self.right_rotate(no)

    def left_rotate(self, node):

        rst_node = node.right
        node.right = rst_node.left

        if rst_node.left is not None:
            rst_node.left.parent = node

        rst_node.parent = node.parent

        if node.parent is None:
            self.root = rst_node
        elif node is node.parent.left:
            node.parent.left = rst_node
        else:
            node.parent.right = rst_node

        rst_node.left = node
        node.parent = rst_node

        node.altura = self.altura(node)
        return rst_node

    def right_rotate(self, node):

        lst_node = node.left
        node.left = lst_node.right

        if lst_node.right is not None:
            lst_node.right.parent = node

        lst_node.parent = node.parent

        if node.parent is None:
            self.root = lst_node
        elif node == node.parent.left:
            node.parent.left = lst_node
        else:
            node.parent.right = lst_node

        lst_node.right = node
        node.parent = lst_node

        node.altura = self.altura(node)
        return lst_node

    def rank(self, no):

        if no.left is None and no.right is None:
            return 0
        if no.left is None:
            return no.right.altura + 1
        if no.right is None:
            return -no.left.altura - 1
        else:
            return no.right.altura - no.left.altura

    def altura(self, no):

        if no.left is None and no.right is None:
            return 0
        if no.left is None:
            return no.right.altura + 1
        if no.right is None:
            return no.left.altura + 1
        else:
            return max(no.right.altura, no.left.altura) + 1

    def buscar_distancia(self, origem, destino):

        if origem == destino:
            return 0

        if self.menor(destino, origem):
            origem, destino = destino, origem

        no_origem = self.search(self.root, origem)

        count = 0
        while True:
            count += 1
            sucessor = self.sucessor(no_origem)
            if sucessor.key == destino:
                return count

            no_origem = sucessor

    def menor(self, a, b):
        tamanho_min = min(len(a), len(b))
        for i in range(tamanho_min):
            if a[i] == b[i]:
                continue
            elif a[i] == "_":
                return True
            elif b[i] == "_":
                return False
            elif a[i] < b[i]:
                return True
            else:
                return False

        if len(a) < len(b):
            return True
        else:
            return False

class Grafo:

    def __init__(self):
        self.no_destinos = {}
        self.visitas = {}
        self.arvore = ArvoreAVL()

    def inserir(self, origem, destino):

        visita_destino = self.visitas.get(destino, None)

        if visita_destino is None:
            self.arvore.inserir(destino)
            visita_destino = [False]
            self.no_destinos[destino] = []
            self.visitas[destino] = visita_destino

        destinos = self.no_destinos.get(origem, None)

        if destinos is not None:
            destinos.append((destino, visita_destino))
        else:
            self.arvore.inserir(origem)
            self.no_destinos[origem] = [(destino, visita_destino)]
            self.visitas[origem] = [False]

    def inserir_sequencial(self):
        no_origem = self.arvore.minimum(self.arvore.root)
        sucessor = self.arvore.sucessor(no_origem)

        while sucessor is not None:
            self.no_destinos[no_origem.key].append((sucessor.key, self.visitas[sucessor.key]))
            self.no_destinos[sucessor.key].append((no_origem.key, self.visitas[no_origem.key]))
            no_origem = sucessor
            sucessor = self.arvore.sucessor(no_origem)

    def distancia (self, origem, destino):

        self.inserir_sequencial()

        fila_1 = [(origem, self.visitas[origem])]
        fila_2 = []

        cont = 0
        while True:
            if len(fila_1) == 0:
                if len(fila_2) == 0:
                    break
                else:
                    fila_1 = fila_2
                    fila_2 = []
                    cont += 1

            origem, visita = fila_1.pop(0)

            if visita[0] == True:
                continue
            else:
                visita[0] = True
                if origem == destino:
                    return cont
                else:
                    fila_2.extend(self.no_destinos[origem])

        return float('inf')

referencias_diretas = int(input())
grafo = Grafo()

for i in range(referencias_diretas):
    grafo.inserir(*input().split())

input()

print(grafo.distancia(*input().split()))


