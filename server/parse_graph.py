from __future__ import print_function
from collections import defaultdict
import re
import sys
import json


class GraphParser(object):
    def parse(self, graph_string):
        lines = graph_string.split('\n')
        graph = defaultdict(list)

        for line in lines:
            try:
                key, value = line.strip(' ;').split(' -> ')
            except ValueError:
                continue

            key = key.strip('"')
            value = value.strip('"')

            graph[key].append(value)

        return graph

    def d3_representation(self, graph):
        nodes = set(graph.keys())
        edges = []
        for start, dests in graph.items():
            for n in dests:
                edges.append((start, n))
                nodes.add(n)

        return list(nodes), edges

if __name__ == '__main__':
    graph_string = sys.stdin.read()

    parser = GraphParser()
    graph = parser.parse(graph_string)

    nodes, edges = parser.d3_representation(graph)

    print(json.dumps({
        'nodes': nodes,
        'edges': edges
        }))
