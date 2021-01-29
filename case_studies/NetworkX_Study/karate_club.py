# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 14:56:35 2020

@author: Dmytro Yermolenko
"""



import networkx as nx
import matplotlib.pyplot as plt

G = nx.karate_club_graph()
nx.draw(G, with_labels=True, node_color="lightblue", edge_color="grey")
plt.savefig("karate_graph.pdf")
print(G.degree())