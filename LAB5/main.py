import time
import xml.etree.ElementTree as ET
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
import math
import heapq
import osmnx as ox

# Скачиваем граф по названию города
G = ox.graph_from_place('Братислава, Словакия', network_type='drive')
# Сохраняем в файл для последующего использования
ox.save_graphml(G, 'bratislava_road_network.graphml')


def haversine(coord1: tuple[float, float], coord2: tuple[float, float]) -> float:
    lon1, lat1 = coord1
    lon2, lat2 = coord2
    R = 6371

    phi1, phi2 = math.radians(lat1), math.radians(lat2)
    dphi = math.radians(lat2 - lat1)
    dlambda = math.radians(lon2 - lon1)

    a = math.sin(dphi / 2) ** 2 + math.cos(phi1) * math.cos(phi2) * math.sin(dlambda / 2) ** 2
    return 2 * R * math.atan2(math.sqrt(a), math.sqrt(1 - a))


def dijkstra(
        graph: dict[tuple[float, float], list[tuple[tuple[float, float], float]]],
        start: tuple[float, float],
        end: tuple[float, float]
) -> tuple[list[tuple[float, float]], float]:
    start_timestamp = time.time()

    shortest_distance = {node: float('inf') for node in graph} # очень неудобно, когда названия переменных длинные,но так надо, ибо программа большая
    previous_node = {node: None for node in graph}
    shortest_distance[start] = 0.0

    # приоритет куае (мин куча)
    min_heap = [(0.0, start)]

    while min_heap:
        current_distance, current = heapq.heappop(min_heap)

        # скипаем
        if current_distance != shortest_distance[current]:
            continue
        # досрок
        if current == end:
            break

        # соседи
        for neighbor, weight in graph.get(current, []):
            distance_candidate = current_distance + weight

            # обнова,если нашли поменьбше
            if distance_candidate < shortest_distance[neighbor]:
                shortest_distance[neighbor] = distance_candidate
                previous_node[neighbor] = current
                heapq.heappush(min_heap, (distance_candidate, neighbor))

    path = []
    total_distance = float('inf')

    if end in previous_node and previous_node[end] is not None:
        total_distance = shortest_distance[end]
        node = end
        while node:
            path.append(node)
            node = previous_node[node]
        path.reverse()
    # точное время в милисекундах (чтоб не было как в прошлой лабе)
    t_ms = (time.time() - start_timestamp) * 1000
    print(f"Алгоритм Дейкстры выполнен за {t_ms:.2f} мс")

    return path, total_distance


def build_graph(edges: list[tuple[tuple[float, float], tuple[float, float], str]]) -> dict[
    tuple[float, float], list[tuple[tuple[float, float], float]]]:
    graph = {}
    for start, end, _ in edges:
        dist = haversine(start, end)
        graph.setdefault(start, []).append((end, dist))
        graph.setdefault(end, []).append((start, dist))
    return graph


def read_graphml(file_path: str) -> tuple[
    dict[str, tuple[float, float]], list[tuple[tuple[float, float], tuple[float, float], str]]]:
    tree = ET.parse(file_path)
    root = tree.getroot()

    namespaces = {'g': 'http://graphml.graphdrawing.org/xmlns'}

    nodes = {}

    for node in root.findall('.//g:node', namespaces):
        node_id = node.get('id')
        x, y = 0.0, 0.0
        for data in node.findall('g:data', namespaces):
            key = data.get('key')
            if key == 'd5':
                x = float(data.text)
            elif key == 'd4':
                y = float(data.text)
        nodes[node_id] = (x, y)

    edges = []
    for edge in root.findall('.//g:edge', namespaces):
        source = edge.get('source')
        target = edge.get('target')
        street_name = ''
        for data in edge.findall('g:data', namespaces):
            if data.get('key') == 'd18':
                street_name = data.text
        if source in nodes and target in nodes:
            edges.append((nodes[source], nodes[target], street_name))

    return nodes, edges


def find_street_index(edges: list[tuple[tuple[float, float], tuple[float, float], str]], street_name_query: str) -> \
tuple[int, str]:
    for i, (_, _, name) in enumerate(edges):
        if name.lower() == street_name_query.lower():
            return i, name

    return -1, None


def visualize_path_with_network(edges, path, street_names=None, figsize=(20, 20)):

    plt.figure(figsize=figsize)
    ax = plt.gca()

    # Все рёбра — серые
    all_lines = [(start, end) for start, end, _ in edges]
    lc = LineCollection(all_lines, linewidths=0.3, colors='gray', alpha=0.4)
    ax.add_collection(lc)

    # Путь — красный
    if path and len(path) > 1:
        path_lines = [(path[i], path[i + 1]) for i in range(len(path) - 1)]
        lc_path = LineCollection(path_lines, linewidths=2.0, colors='red', alpha=0.9)
        ax.add_collection(lc_path)

        # Отображаем названия улиц, если они заданы (я не поняла, как их вытащить в дейкстре)
        if street_names:
            for i in range(len(path) - 1):
                mid_point = ((path[i][0] + path[i + 1][0]) / 2, (path[i][1] + path[i + 1][1]) / 2)
                if i < len(street_names) and street_names[i]:
                    plt.text(mid_point[0], mid_point[1], street_names[i],
                             fontsize=8, color='blue', ha='center')

    ax.autoscale()
    plt.axis('equal')
    plt.title('Кратчайший маршрут')
    plt.xlabel('Долгота')
    plt.ylabel('Широта')
    plt.grid(False)
    plt.tight_layout()
    plt.show()


def visualize_only_path(path, figsize=(10, 10)):
    if not path or len(path) < 2:
        print("Маршрут слишком короткий или отсутствует.")
        return

    plt.figure(figsize=figsize)
    ax = plt.gca()

    path_lines = [(path[i], path[i + 1]) for i in range(len(path) - 1)]
    lc_path = LineCollection(path_lines, linewidths=2.5, colors='red', alpha=0.9)
    ax.add_collection(lc_path)

    ax.autoscale()
    plt.axis('equal')
    plt.title("Кратчайший маршрут")
    plt.xlabel("Долгота")
    plt.ylabel("Широта")
    plt.grid(True)
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    nodes, edges = read_graphml("bratislava_road_network.graphml")

    start_street_query = "Černyševského"
    end_street_query = "Stredná"

    start_index, start_street = find_street_index(edges, start_street_query)
    end_index, end_street = find_street_index(edges, end_street_query)

    if start_index == -1 or end_index == -1:
        print("Не удалось найти заданную улицу для начала или конца маршрута")
    else:
        start_node = edges[start_index][0]
        end_node = edges[end_index][1]

        graph = build_graph(edges)
        path, distance = dijkstra(graph, start_node, end_node)

        if not path:
            print("Путь не найден")
        else:
            print(f"Найден путь длиной {distance:.2f} км")
            print(f"Вершин/Ребер {len(nodes)}/{len(edges)}")

            visualize_path_with_network(edges, path)
