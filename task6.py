class Graph:
    def __init__(self, size):
        self.size = size
        self.edges = [] # храним все рёбра в виде (откуда, куда, вес)

    def add_edge(self, u, v, w):
        self.edges.append((u, v, w)) # кидаем ребро в список

    def bellman_ford(self, point):
        INF = float('inf')

        dist = [INF] * self.size # расстояния до всех вершин
        parent = [None] * self.size # откуда пришли (восстанавливаем путь)
        dist[point] = 0 # от стартовой вершины до неё же 0

        # делаем size-1 проходов
        for i in range(self.size - 1):
            upd = False
            for u, v, w in self.edges:
                if dist[u] == INF: # до этой вершины еще не дошли, пропускаем
                    continue
                if dist[u] + w < dist[v]: # нашли путь короче, обновляем
                    dist[v] = dist[u] + w
                    parent[v] = u
                    upd = True
            if not upd: # если за весь проход ничего не обновилось, дальше смысла нет
                break

        # делаем еще один (size-й) проход: если что-то обновилось — значит есть минусовой цикл
        neg = False
        for u, v, w in self.edges:
            if dist[u] == INF:
                continue
            if dist[u] + w < dist[v]:
                neg = True
                break

        return dist, parent, neg

    def neg_cycle_nums(self, point):
        INF = float('inf')
        dist, parent, neg = self.bellman_ford(point)
        if not neg:
            return None # цикла нет — возвращаем None

        # ищем вершину, которую можно расслабить еще раз. Она 100% лежит на цикле или после него
        node = None
        for u, v, w in self.edges:
            if dist[u] == INF:
                continue
            if dist[u] + w < dist[v]:
                node = v
                break

        # откатываемся назад по parent ровно size раз. Это гарантирует, что мы попадем внутрь цикла
        for i in range(self.size):
            node = parent[node]

        # теперь крутимся по parent и собираем сам цикл
        cycle = []
        start = node
        while True:
            cycle.append(node)
            node = parent[node]
            if node == start: # вернулись в начало — хватит
                break
        cycle.append(start) # замыкаем цикл
        cycle.reverse() # разворачиваем, т.к. шли задом наперед
        return cycle

    def way(self, parent, point, target):
        if parent[target] is None and target != point:
            return [] # пути нет (даже parent не записан)
        way = []
        node = target
        while node is not None: # идем от цели обратно к старту по parent
            way.append(node)
            if node == point:
                break
            node = parent[node]
        way.reverse() # разворачиваем, чтобы было от старта к цели
        return way

'''
g = Graph(4)
g.add_edge(0, 1, 4)
g.add_edge(0, 3, 5)
g.add_edge(1, 2, -3)
g.add_edge(3, 2, 2)

dist, parent, neg = g.bellman_ford(0)
print("Расстояния от 0:", dist)
print("Отрицательный цикл:", neg)
print("Путь 0 -> 2:", g.way(parent, 0, 2))
'''
g2 = Graph(4)
g2.add_edge(0, 1, 1)
g2.add_edge(1, 2, -1)
g2.add_edge(2, 1, -1)
g2.add_edge(0, 3, 5)
g2.add_edge(3, 2, 2)
print("g2.edges:", g2.edges)
dist2, parent2, neg2 = g2.bellman_ford(0)
print("Расстояния:", dist2)
print("Отрицательный цикл:", neg2)
print("Вершины цикла:", g2.neg_cycle_nums(0))