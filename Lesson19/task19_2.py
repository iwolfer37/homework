import csv
import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

# Зчитування даних з файлу та додавання їх до графу
with open('cities.csv', newline='', encoding='cp1251') as csvfile:
    reader = csv.reader(csvfile, delimiter=';')
    for row in reader:
        city1, city2, distance = row
        G.add_edge(city1, city2, distance=int(distance))

# пошук найкоротшого шляху
def shortest_path(graph, start, end):
    path = nx.shortest_path(graph, start, end)
    distance = nx.shortest_path_length(graph, start, end)
    return path, distance

# Приклад виклику функції
path, distance = shortest_path(G, 'Kyiv', 'Rivne')
print("Найкоротший маршрут:", path)
print("Протяжність маршруту:", distance)
