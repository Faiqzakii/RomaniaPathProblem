#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Sat Jan 25 02:14:44 2020

@author: faiqzakii
"""

GRAPH = {
            'Arad': {'Zerind': 75, 'Timisoara': 118, 'Sibiu': 140},
            'Zerind': {'Arad': 75, 'Oradea': 71},
            'Oradea': {'Zerind': 71, 'Sibiu': 151},
            'Sibiu': {'Arad': 140, 'Oradea': 151, 'Fagaras': 99, 'Rimnicu': 80},
            'Timisoara': {'Arad': 118, 'Lugoj': 111},
            'Lugoj': {'Timisoara': 111, 'Mehadia': 70},
            'Mehadia': {'Lugoj': 70, 'Drobeta': 75},
            'Drobeta': {'Mehadia': 75, 'Craiova': 120},
            'Craiova': {'Drobeta': 120, 'Rimnicu': 146, 'Pitesti': 138},
            'Rimnicu': {'Sibiu': 80, 'Craiova': 146, 'Pitesti': 97},
            'Fagaras': {'Sibiu': 99, 'Bucharest': 211},
            'Pitesti': {'Rimnicu': 97, 'Craiova': 138, 'Bucharest': 101},
            'Bucharest': {'Fagaras': 211, 'Pitesti': 101, 'Giurgiu': 90, 'Urziceni': 85},
            'Giurgiu': {'Bucharest': 90},
            'Urziceni': {'Bucharest': 85, 'Vaslui': 142, 'Hirsova': 98},
            'Hirsova': {'Urziceni': 98, 'Eforie': 86},
            'Eforie': {'Hirsova': 86},
            'Vaslui': {'Iasi': 92, 'Urziceni': 142},
            'Iasi': {'Vaslui': 92, 'Neamt': 87},
            'Neamt': {'Iasi': 87}
        }

def bf_search(graph, start, goal):
    explored = []
    queue = [[start]]

    if start == goal:
        return("Start dan Goal merupakan titik yang sama")

    while queue:
        #Breadth First Search itu First in First out, jadi queue pertama di copy menjadi path dan dibuang dari queue list
        path = queue.pop(0)

        #Mengambil node terakhir dari path atau bisa dibilang queue yang dibuang tadi
        node = path[-1]

        if node not in explored:
            #Mengambil node yang berhubungan dengan node yang dipilih
            neighbours = graph[node]

            for neighbour in neighbours:
                #Copy path dan diubah menjadi list
                current_path = list(path)

                #Append neighbour node kedalam path
                current_path.append(neighbour)

                #Masukkan antrian baru
                queue.append(current_path)

                #Mengeluarkan path saat ini dan di print
                yield current_path

                if neighbour == goal:
                    return

            explored.append(node)

def df_search(graph, start, goal):
    explored = []
    stack = [[start]]

    if start == goal:
        return("Start dan Goal merupakan titik yang sama")

    while stack:
        #Depth First Search itu Last in First out, jadi queue pertama di copy menjadi path dan dibuang dari queue list
        path = stack.pop()

        #Mengambil node terakhir dari path atau bisa dibilang queue yang dibuang tadi
        node = path[-1]

        if node not in explored:
            #Mengambil node yang berhubungan dengan node yang dipilih
            neighbours = graph[node]

            for neighbour in neighbours:
                #Copy path dan diubah menjadi list
                current_path = list(path)

                #Append neighbour node kedalam path
                current_path.append(neighbour)

                #Masukkan antrian baru
                stack.append(current_path)

                #Mengeluarkan path saat ini dan di print
                yield current_path

                if neighbour == goal:
                    return

            explored.append(node)

def df__limited_search(graph, start, goal, limit = 5):
    explored = []
    stack = [[start]]

    if start == goal:
        return("Start dan Goal merupakan titik yang sama")

    while stack:
        #Depth First Search itu Last in First out, jadi queue pertama di copy menjadi path dan dibuang dari queue list
        path = stack.pop()

        #Mengambil node terakhir dari path atau bisa dibilang queue yang dibuang tadi
        node = path[-1]

        if len(path)<=limit:
            if node not in explored:
                #Mengambil node yang berhubungan dengan node yang dipilih
                neighbours = graph[node]

                for neighbour in neighbours:
                    #Copy path dan diubah menjadi list
                    current_path = list(path)

                    #Append neighbour node kedalam path
                    current_path.append(neighbour)

                    #Masukkan antrian baru
                    stack.append(current_path)

                    #Mengeluarkan path saat ini dan di print
                    yield current_path

                    if neighbour == goal:
                        return

                explored.append(node)
        else:
            continue

    if current_path[-1] == goal:
        return
    else:
        print('Tidak terdapat jalur menuju {} dalam {} langkah'.format(goal, limit))

def uc_search(graph, start, goal):
    from queue import PriorityQueue

    prior_queue = PriorityQueue()
    explored = {}

    """parameter PriorityQueue (cost so far, node yang dikunjungi saat ini, path yang telah dilalui) """
    prior_queue.put((0, start, [start]))
    explored[start] = 0

    while prior_queue:
        (cost, node, path) = prior_queue.get()

        if node == goal:
            return cost, path

        for neighbour in graph[node].keys():
            current_cost = cost + graph[node][neighbour]

            if neighbour not in explored or explored[neighbour] >= current_cost:
                explored[neighbour] = current_cost
                prior_queue.put((current_cost, neighbour, path + [neighbour]))

def main():
    start = input("Tentukan titik awal perjalanan: ")
    goal = input("Tentukan titik tujuan perjalanan: ")
    if start not in GRAPH or goal not in GRAPH:
        print('Error, kota asal atau kota tujuan tidak ditemukan')
    else:
        print("\nBreadth First Search: ")
        bf_path = bf_search(GRAPH, start, goal)
        i = 1
        for path in bf_path:
            print('Pencarian ke-'+ str(i) + ': ' + ' -> '.join(city for city in path))
            i = i+1

        print("\nDepth First Search: ")
        df_path = df_search(GRAPH, start, goal)
        i = 1
        for path in df_path:
            print('Pencarian ke-'+ str(i) + ': ' + ' -> '.join(city for city in path))
            i = i+1

        print("\nLimited Depth First Search: ")
        limit = int(input("Maksimal berapa langkah? "))
        df_limit_path = df__limited_search(GRAPH, start, goal, limit)
        i = 1
        for path in df_limit_path:
            print('Pencarian ke-'+ str(i) + ': ' + ' -> '.join(city for city in path))
            i = i+1

        print("\nUniform Cost Search: ")
        cost, uc_path = uc_search(GRAPH, 'Arad', 'Bucharest')
        print('Cheapest Path: ' + ' -> '.join(city for city in uc_path))
        print('Path Cost: ' + str(cost))

if __name__ == '__main__':
    main()
