import csv
import networkx as nx
import matplotlib.pyplot as plt

# Створення графу
G = nx.Graph()

with open('cities.csv', newline='', encoding='cp1251') as csvfile:
    reader = csv.reader(csvfile, delimiter=';')
    for row in reader:
        city1, city2, distance = row
        G.add_edge(city1, city2, distance=int(distance))

# Візуалізація графу
nx.draw(G, with_labels=True)
plt.show()
