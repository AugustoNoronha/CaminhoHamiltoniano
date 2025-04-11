class Grafo:
    def __init__(self, vertices, direcionado=False):
        self.V = vertices
        self.grafo = {v: [] for v in range(vertices)}
        self.direcionado = direcionado
    
    def adicionar_aresta(self, u, v):
        self.grafo[u].append(v)
        if not self.direcionado:
            self.grafo[v].append(u)
    
    def eh_seguro(self, v, pos, caminho):
        if v not in self.grafo[caminho[pos-1]]:
            return False
        
        if v in caminho:
            return False
            
        return True
    
    def encontrar_caminho_hamiltoniano_util(self, caminho, pos):
        if pos == self.V:
            return True
            
        for v in range(self.V):
            if self.eh_seguro(v, pos, caminho):
                caminho[pos] = v
                
                if self.encontrar_caminho_hamiltoniano_util(caminho, pos+1):
                    return True
                
                caminho[pos] = -1
                
        return False
    
    def encontrar_caminho_hamiltoniano(self):
        caminho = [-1] * self.V
        
        for inicio in range(self.V):
            caminho[0] = inicio
            
            if self.encontrar_caminho_hamiltoniano_util(caminho, 1):
                return caminho
                
        print("Não existe caminho hamiltoniano")
        return None

if __name__ == "__main__":
    g = Grafo(5, direcionado=False)
    g.adicionar_aresta(0, 1)
    g.adicionar_aresta(0, 3)
    g.adicionar_aresta(1, 2)
    g.adicionar_aresta(1, 3)
    g.adicionar_aresta(1, 4)
    g.adicionar_aresta(2, 4)
    g.adicionar_aresta(3, 4)
    
    caminho = g.encontrar_caminho_hamiltoniano()
    
    if caminho:
        print("Caminho Hamiltoniano encontrado:")
        print(" => ".join(map(str, caminho)))
    else:
        print("Nenhum caminho hamiltoniano encontrado")