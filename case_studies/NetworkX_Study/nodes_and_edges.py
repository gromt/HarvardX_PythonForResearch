# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 14:21:08 2020

@author: Dmytro Yermolenko
"""


import networkx as nx

G = nx.Graph()
G.add_node(1)
G.add_nodes_from([2,3])
G.add_nodes_from(["u","v"])
G.add_edge(1,2)
G.add_edge("u","v")
G.add_edges_from([(1,3), (1,4), (1,5), (1,6)])
G.add_edge("u","w")
G.remove_node(2)
G.remove_nodes_from([4,5])
G.remove_edge(1,3)
G.remove_edges_from([(1,2),("u","v")])
G.number_of_nodes()
G.number_of_edges()
G.nodes()
G.edges()