
# Hamiltonian Path Finder

## Execução
Para executar o código, abra o terminal (cmd) no diretório onde está localizado o arquivo `main.py` e utilize o comando:
```bash
python main.py
```

---

## Explicação linha a linha

1. `class Grafo:`  
   - Define a classe Grafo que representa a estrutura de um grafo.

2. `def __init__(self, vertices, direcionado=False):`  
   - Construtor da classe. Recebe o número de vértices e um booleano para indicar se o grafo é direcionado.

3. `self.V = vertices`  
   - Armazena a quantidade de vértices.

4. `self.grafo = {v: [] for v in range(vertices)}`  
   - Inicializa o grafo como um dicionário de listas de adjacência.

5. `self.direcionado = direcionado`  
   - Define se o grafo é direcionado.

6. `def adicionar_aresta(self, u, v):`  
   - Método para adicionar arestas entre os vértices u e v.

7. `self.grafo[u].append(v)`  
   - Adiciona v à lista de adjacência de u.

8. `if not self.direcionado: self.grafo[v].append(u)`  
   - Se o grafo for não direcionado, adiciona u à lista de adjacência de v.

9. `def eh_seguro(self, v, pos, caminho):`  
   - Verifica se é seguro adicionar o vértice v na posição `pos` do caminho.

10. `if v not in self.grafo[caminho[pos-1]]:`  
    - Verifica se v está conectado ao último vértice adicionado no caminho.

11. `if v in caminho:`  
    - Garante que o vértice v ainda não foi visitado.

12. `return True`  
    - Se passar pelas duas verificações, retorna True.

13. `def encontrar_caminho_hamiltoniano_util(self, caminho, pos):`  
    - Função recursiva para tentar encontrar o caminho Hamiltoniano.

14. `if pos == self.V:`  
    - Caso base: se a posição atual for igual ao número de vértices, o caminho está completo.

15. `for v in range(self.V):`  
    - Itera sobre todos os vértices para tentar encontrar o próximo vértice válido.

16. `if self.eh_seguro(v, pos, caminho): caminho[pos] = v`  
    - Se for seguro, coloca v no caminho.

17. `if self.encontrar_caminho_hamiltoniano_util(caminho, pos+1):`  
    - Chamada recursiva com a próxima posição.

18. `caminho[pos] = -1`  
    - Backtracking: remove o vértice atual se não levou a uma solução.

19. `def encontrar_caminho_hamiltoniano(self):`  
    - Inicializa o caminho e tenta encontrar um caminho Hamiltoniano a partir de cada vértice.

20. `for inicio in range(self.V):`  
    - Tenta iniciar o caminho por cada vértice do grafo.

21. `if self.encontrar_caminho_hamiltoniano_util(caminho, 1): return caminho`  
    - Se encontrar um caminho válido, retorna-o.

22. `return None`  
    - Se não encontrar, retorna None.

23. `if __name__ == "__main__":`  
    - Bloco principal que executa o código quando o arquivo é rodado diretamente.

24. `g = Grafo(5, direcionado=False)`  
    - Cria um grafo não direcionado com 5 vértices.

25. `g.adicionar_aresta(...)`  
    - Adiciona as arestas especificadas ao grafo.

26. `caminho = g.encontrar_caminho_hamiltoniano()`  
    - Chama o método para buscar um caminho Hamiltoniano.

27. `print(...)`  
    - Exibe o caminho encontrado ou informa que não foi encontrado.

---

## Relatório Técnico

### Classes P, NP, NP-Completo e NP-Difícil

1. **Classificação do problema:**  
   O problema do **Caminho Hamiltoniano** está na classe **NP-Completo**.

2. **Justificativa:**  
   - O problema pertence à classe NP porque uma solução pode ser verificada em tempo polinomial.  
   - É NP-Completo pois qualquer problema em NP pode ser reduzido a ele em tempo polinomial.  
   - Relaciona-se diretamente com o **Problema do Caixeiro Viajante (TSP)**, que também é NP-Completo. A diferença é que no TSP há pesos e o objetivo é minimizar o custo, enquanto no Caminho Hamiltoniano buscamos apenas a existência de um caminho que passe por todos os vértices uma única vez.

---

### Análise da complexidade assintótica de tempo

1. **Complexidade temporal:**  
   A complexidade do algoritmo é **O(V!)**, onde V é o número de vértices.

2. **Método de determinação:**  
   - Utilizamos a **contagem de operações**.  
   - A função `encontrar_caminho_hamiltoniano_util` tenta todos os possíveis caminhos, o que gera uma árvore de recursão com ramificações de ordem fatorial, já que cada posição pode ter múltiplas possibilidades dependendo do grafo.

---

### Aplicação do Teorema Mestre

- **Aplicabilidade:**  
  Não é possível aplicar o Teorema Mestre neste caso.

- **Justificativa:**  
  O Teorema Mestre é utilizado para resolver recorrências do tipo:
  `T(n) = aT(n/b) + f(n)`  
  Neste caso, a recursão não é baseada em divisão do problema em subproblemas menores com tamanho proporcional. O número de possibilidades depende das combinações de vértices, não da divisão de dados.

---

### Análise dos casos de complexidade

1. **Melhor caso:**  
   - Um caminho Hamiltoniano é encontrado logo nas primeiras tentativas.  
   - Complexidade ainda é O(V!), mas na prática o tempo é reduzido pela poda.

2. **Caso médio:**  
   - A média das execuções em diferentes grafos gera tentativa e erro com backtracking, ainda com complexidade O(V!).

3. **Pior caso:**  
   - Não existe caminho Hamiltoniano, e o algoritmo tenta **todas as combinações possíveis**.  
   - Tempo máximo de execução: **O(V!)**.

4. **Impacto no desempenho:**  
   - A variação entre os casos pode impactar severamente o tempo de execução. O algoritmo não possui otimizações para evitar repetir estados ou reduzir a árvore de busca.
