#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Sat Jan 29 00:09:39 2020

@author: faiqzakii
"""

from queue import PriorityQueue

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

straigth_line = {
                    'Arad' : 366,
                    'Bucharest' : 0,
                    'Craiova' : 160,
                    'Drobeta' : 242,
                    'Eforie' : 161,
                    'Fagaras' : 176,
                    'Giurgiu' : 77,
                    'Hirsova' : 151,
                    'Iasi' : 226,
                    'Lugoj' : 244,
                    'Mehadia' : 241,
                    'Neamt' : 234,
                    'Oradea' : 380,
                    'Pitesti' : 100,
                    'Rimnicu' : 193,
                    'Sibiu' : 253,
                    'Timisoara' : 329,
                    'Urziceni' : 80,
                    'Vaslui' : 199,
                    'Zerind' : 374
                }

def greedy(graph, start, goal):
    prior_queue = PriorityQueue()
    explored = {}

    prior_queue.put((straigth_line[start], start, [start]))
    explored[start] = straigth_line[start]

    while prior_queue:
        heuristic, node, path = prior_queue.get()

        if node == goal:
            return path

        for neighbour in graph[node].keys():
            heuristic = straigth_line[neighbour]
            print(path + [neighbour])

            if neighbour not in explored:
                prior_queue.put((heuristic, neighbour, path + [neighbour]))

    if node != goal:
        return("Tidak ada jalur yang dapat dilewati")
    
def astar(graph, start, goal):
    prior_queue = PriorityQueue()
    explored = {}

    """Parameter PriorityQueue (heuristic information, cost so far, node saat ini, path yang telah dilalui)"""
    prior_queue.put((straigth_line[start], 0, start, [start]))

    explored[start] = straigth_line[start]

    while prior_queue:
        (heuristic, cost, node, path) = prior_queue.get()

        if node == goal:
            return heuristic, cost, path

        for neighbour in graph[node].keys():
            current_cost = cost + graph[node][neighbour]
            heuristic = current_cost + straigth_line[neighbour]
            print(path + [neighbour])

            if neighbour not in explored or explored[neighbour] >= heuristic:
                explored[neighbour] = heuristic
                prior_queue.put((heuristic, current_cost, neighbour, path + [neighbour]))

    if node != goal:
        return("Tidak ada jalur yang dapat dilewati")

def main():
    start = input("Tentukan titik awal perjalanan: ")
    goal = input("Tentukan titik tujuan perjalanan: ")
    if start not in GRAPH or goal not in GRAPH:
        print('Error, kota asal atau kota tujuan tidak ditemukan')
    else:
        print("\nGreedy Search: ")
        greedy_path = greedy(GRAPH, start, goal)
        print('Cheapest Path: ' + ' -> '.join(city for city in greedy_path))

        print("\nA* Search: ")
        heuristic, cost, astar_path = astar(GRAPH, start, goal)
        print('Cheapest Path: ' + ' -> '.join(city for city in astar_path))
        print('Estimated Path Cost(Heuristic): ' + str(heuristic))
        print('Path Cost: ' + str(cost))

if __name__ == '__main__':
    main()
