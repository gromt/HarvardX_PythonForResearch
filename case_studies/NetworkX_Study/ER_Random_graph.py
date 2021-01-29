# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 15:16:57 2020

@author: Dmytro Yermolenko
"""

import matplotlib.pyplot as plt
from scipy.stats import bernoulli # bernoulli.rvs(p=0.2)
import networkx as nx

def er_graph(N, p):
    """ Generate an ER graph. """
    G = nx.Graph()
    G.add_nodes_from(range(N))
    for node1 in G.nodes():
        for node2 in G.nodes():
            if node1 < node2 and bernoulli.rvs(p=p):
                G.add_edge(node1, node2)
    return G

plt.figure()                
nx.draw(er_graph(50, 0.08), node_size=40, node_color="gray")
plt.savefig("er1.pdf")

plt.figure()  
ER = nx.erdos_renyi_graph(10, 1)
nx.draw(ER)
plt.savefig("er2.pdf")
