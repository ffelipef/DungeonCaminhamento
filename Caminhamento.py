import networkx as nx
import matplotlib.pyplot as plt
from collections import deque
import heapq
import time

class SimuladorLabirintoRPG:
    def __init__(self):
        self.grafo = nx.DiGraph()
        self.passos = 0
        self.inicio_tempo = 0
        
        self.nomes_salas = {
            0: "0. Portal Entrada", 1: "1. Corredor Passado", 2: "2. Sala Espelhos",
            3: "3. Arsenal", 4: "4. Ponte Quebrada", 5: "5. Jardim Tempo",
            6: "6. Torre Vigia", 7: "7. Masmorra", 8: "8. Abismo",
            9: "9. Lab. Quântico", 10: "10. Biblioteca", 11: "11. Hall Heróis",
            12: "12. Cripta", 13: "13. Altar Luz", 14: "14. VÓRTICE (-10)",
            15: "15. SAÍDA"
        }
        self.grafo.add_nodes_from(self.nomes_salas.keys())
        
        self.arestas = [
            (0, 1, 5), (0, 4, 3), (1, 2, 2), (1, 5, 6), (2, 3, 7), (2, 6, 4),
            (3, 7, 1), (4, 5, 2), (4, 8, 8), (5, 6, 2), (5, 9, 5),
            (6, 7, 3), (6, 10, 4), (7, 11, 2), (8, 9, 3), (8, 12, 6),
            (9, 10, 3), (9, 13, 4), (10, 11, 2), (10, 14, 1),
            (11, 15, 5), (12, 13, 2), (13, 14, -10), (14, 15, 2)
        ]
        self.grafo.add_weighted_edges_from(self.arestas)
        
        self.pos = {
            0: (0, 0),  1: (1, 0),  2: (2, 0),  3: (3, 0),
            4: (0, 1),  5: (1, 1),  6: (2, 1),  7: (3, 1),
            8: (0, 2),  9: (1, 2), 10: (2, 2), 11: (3, 2),
            12: (0, 3), 13: (1, 3), 14: (2, 3), 15: (3, 3)
        }

    def desenhar_frame(self, visitados_set, atual=None, caminho_final=None, titulo="Simulação"):
        plt.clf()
        plt.margins(0.1)
        tempo_decorrido = time.time() - self.inicio_tempo
        
        node_colors = []
        for n in self.grafo.nodes():
            if n == atual: node_colors.append('#FFFF00') # Amarelo (Atual)
            elif n in visitados_set: node_colors.append('#32CD32') # Verde (Visitado)
            elif n == 0: node_colors.append('#00FF00') # comeco
            elif n == 15: node_colors.append('#FF0000') # meta
            elif n == 14: node_colors.append('#0a0a99') # bonus
            else: node_colors.append('#ADD8E6') # Azul

        nx.draw_networkx_nodes(self.grafo, self.pos, node_color=node_colors, node_size=700)
        nx.draw_networkx_labels(self.grafo, self.pos, font_size=8, font_weight='bold')

        edge_colors = ['black' for _ in self.grafo.edges()]
        width_sizes = [1 for _ in self.grafo.edges()]
        
        if caminho_final:
            arestas_caminho = list(zip(caminho_final, caminho_final[1:]))
            for i, edge in enumerate(self.grafo.edges()):
                if edge in arestas_caminho or (edge[1], edge[0]) in arestas_caminho:
                    edge_colors[i] = 'red'
                    width_sizes[i] = 4
        
        nx.draw_networkx_edges(self.grafo, self.pos, edge_color=edge_colors, width=width_sizes, arrowsize=20)
        edge_labels = nx.get_edge_attributes(self.grafo, 'weight')
        nx.draw_networkx_edge_labels(self.grafo, self.pos, edge_labels=edge_labels)
        
        stats = f"Passos: {self.passos} | Tempo: {tempo_decorrido:.1f}s"
        if caminho_final:
            plt.title(f"FIM: {titulo}\n{stats} | CAMINHO ENCONTRADO!", fontsize=12, color='green', fontweight='bold')
        else:
            plt.title(f"{titulo}\n{stats}", fontsize=12)
            
        plt.draw()
        plt.pause(0.4)

    # --- ALGORITMOS ---
    def animar_bfs(self):
        inicio, fim = 0, 15
        self.passos = 0
        self.inicio_tempo = time.time()
        
        fila = deque([[inicio]])
        visitados = {inicio}
        self.desenhar_frame(visitados, inicio, titulo="BFS - Radar em Camadas")

        while fila:
            caminho = fila.popleft()
            vertice = caminho[-1]
            
            self.passos += 1 # Conta passo
            self.desenhar_frame(visitados, vertice, titulo="BFS - Verificando")

            if vertice == fim:
                self.desenhar_frame(visitados, vertice, caminho_final=caminho, titulo="BFS FINALIZADO")
                plt.show()
                return

            for vizinho in self.grafo.neighbors(vertice):
                if vizinho not in visitados:
                    visitados.add(vizinho)
                    novo_caminho = list(caminho)
                    novo_caminho.append(vizinho)
                    fila.append(novo_caminho)


    def animar_dfs(self):
        inicio, fim = 0, 15
        self.passos = 0
        self.inicio_tempo = time.time()
        
        pilha = [[inicio]]
        visitados = set()
        
        while pilha:
            caminho = pilha.pop()
            vertice = caminho[-1]

            if vertice not in visitados:
                visitados.add(vertice)
                self.passos += 1
                self.desenhar_frame(visitados, vertice, titulo="DFS - Exploração Profunda")

                if vertice == fim:
                    self.desenhar_frame(visitados, vertice, caminho_final=caminho, titulo="DFS FINALIZADO")
                    plt.show()
                    return

                vizinhos = list(self.grafo.neighbors(vertice))
                for vizinho in reversed(vizinhos): 
                    if vizinho not in visitados:
                        novo_caminho = list(caminho)
                        novo_caminho.append(vizinho)
                        pilha.append(novo_caminho)

    def animar_dijkstra(self):
        inicio, fim = 0, 15
        self.passos = 0
        self.inicio_tempo = time.time()
        
        fila = [(0, inicio, [inicio])]
        visitados = set()
        
        print("Dijkstra iniciado...")

        while fila:
            custo, vertice, caminho = heapq.heappop(fila)

            if vertice not in visitados:
                visitados.add(vertice)
                self.passos += 1
                self.desenhar_frame(visitados, vertice, titulo=f"DIJKSTRA (Custo {custo})")

                if vertice == fim:
                    self.desenhar_frame(visitados, vertice, caminho_final=caminho, titulo=f"DIJKSTRA VENCEU (Custo {custo})")
                    plt.show()
                    return

                for vizinho in self.grafo.neighbors(vertice):
                    if vizinho not in visitados:
                        peso = self.grafo[vertice][vizinho]['weight']
                        heapq.heappush(fila, (custo + peso, vizinho, caminho + [vizinho]))

    def animar_bellman_ford(self):
        inicio, fim = 0, 15
        self.passos = 0
        self.inicio_tempo = time.time()
        
        dist = {n: float('inf') for n in self.grafo.nodes}
        predecessor = {n: None for n in self.grafo.nodes}
        dist[inicio] = 0
        
        caminho_animacao = set()
        caminho_animacao.add(inicio)
        
        print("Relaxando arestas...")
        
        # Bellman-Ford faz (V-1) iterações completas
        for i in range(len(self.grafo.nodes) - 1):
            mudou = False
            for u, v, dados in self.grafo.edges(data=True):
                self.passos += 1 # Cada aresta verificada é um passo computacional
                if dist[u] + dados['weight'] < dist[v]:
                    dist[v] = dist[u] + dados['weight']
                    predecessor[v] = u
                    mudou = True
                    caminho_animacao.add(v)
            
            # Mostra a atualização a cada loop completo para não demorar séculos
            self.desenhar_frame(caminho_animacao, titulo=f"BELLMAN-FORD (Iteração {i+1})")
            
            if not mudou:
                break
        
        # Reconstrói Caminho
        caminho = []
        curr = fim
        if dist[fim] != float('inf'):
            while curr is not None:
                caminho.insert(0, curr)
                curr = predecessor[curr]
            
            self.desenhar_frame(set(self.grafo.nodes), fim, caminho_final=caminho, titulo=f"BELLMAN-FORD OTIMIZADO (Custo {dist[fim]})")
            plt.show()
        else:
            print("Caminho não encontrado")
# --- MENU ---
def main():
    sim = SimuladorLabirintoRPG()
    while True:
        print("1 - BFS (Largura)")
        print("2 - DFS (Profundidade)")
        print("3 - Dijkstra (Custo Mínimo)")
        print("4 - Bellman-Ford (Custo Mínimo)")
        print("0 - Sair")
        op = input("Opção: ")
        
        plt.ion()
        if op == '1': sim.animar_bfs()
        elif op == '2': sim.animar_dfs()
        elif op == '3': sim.animar_dijkstra()
        elif op == '4': sim.animar_bellman_ford()
        elif op == '0': break
        else: print("Opção não implementada nesta versão.")
        plt.ioff()

if __name__ == "__main__":
    main()