# Simulador de Logística Temporal com Grafos (Teoria de Grafos)

Este projeto implementa e compara algoritmos de caminhamento em grafos (BFS, DFS, Dijkstra e Bellman-Ford) aplicados a um cenário fictício de "Logística Temporal", onde arestas de peso negativo representam ganho de recursos.

Desenvolvido como requisito avaliativo da disciplina de Teoria de Grafos.

## 📋 Funcionalidades
- **Visualização Gráfica:** Renderização do grafo utilizando `networkx` e `matplotlib`.
- **Animação em Tempo Real:** Acompanhamento passo-a-passo da execução dos algoritmos.
- **Métricas de Desempenho:** Exibição de passos (iterações) e tempo de simulação.
- **Cenário Complexo:** Grafo com 16 vértices e arestas de peso negativo para validar o algoritmo de Bellman-Ford.

## 🚀 Como Executar

### Pré-requisitos
Certifique-se de ter o Python 3.8+ instalado.

### Instalação
1. Clone o repositório:
   ```bash
   git clone [https://github.com/SEU_USUARIO/Graph-Theory-Simulator.git](https://github.com/SEU_USUARIO/Graph-Theory-Simulator.git)
   cd Graph-Theory-Simulator
   ```
2. Instale as dependências
   ```bash
   pip install -r requirements.txt
   ```
3. Rodando o Simulador
Execute o arquivo principal:
  ```bash
  python simulador_grafos.py
  ```
Um menu interativo aparecerá no terminal. Selecione o algoritmo desejado (1-4) para iniciar a visualização.

## 🧪 Algoritmos Comparados
1. BFS (Busca em Largura): Foca no menor número de saltos.

2. DFS (Busca em Profundidade): Exploração topológica exaustiva.

3. Dijkstra: Busca de custo mínimo (falha em otimizar rotas com pesos negativos).

4. Bellman-Ford: Busca de custo mínimo otimizada para arbitragem (detecta e utiliza o peso -10).
