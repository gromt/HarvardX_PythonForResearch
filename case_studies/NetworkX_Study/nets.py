# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 14:07:20 2020

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

def plot_degree_distribution(G):
    degree_sequence = [d for n, d in G.degree()]
    plt.hist(degree_sequence, histtype="step")
    plt.xlabel("Degree $k$")    
    plt.ylabel("$P(k)$")
    plt.title("Degree distribution")
    
# G1 = er_graph(500, 0.08)
# plot_degree_distribution(G1)
# G2 = er_graph(500, 0.08)
# plot_degree_distribution(G2)
# G3 = er_graph(500, 0.08)
# plot_degree_distribution(G3)
# plt.savefig("hist_3.pdf")

plot_degree_distribution(nx.erdos_renyi_graph(100, 0.3))