# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 13:06:25 2020

@author: Dmytro Yermolenko
"""


import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

A1 = np.loadtxt("adj_allVillageRelationships_vilno_1.csv", delimiter=",")
A2 = np.loadtxt("adj_allVillageRelationships_vilno_2.csv", delimiter=",")

G1 = nx.to_networkx_graph(A1)
G2 = nx.to_networkx_graph(A2)

def basic_net_stats(G):
    print("Number of nodes: %d" % G.number_of_nodes())
    print("Number of edges: %d" % G.number_of_edges())
    degree_sequence = [d for n, d in G.degree()]
    print("Average degree: %.2f" % np.mean(degree_sequence))
    
def plot_degree_distribution(G):
    degree_sequence = [d for n, d in G.degree()]
    plt.hist(degree_sequence, histtype="step")
    plt.xlabel("Degree $k$")    
    plt.ylabel("$P(k)$")
    plt.title("Degree distribution")
    
basic_net_stats(G1)
basic_net_stats(G2)

plot_degree_distribution(G1)
plot_degree_distribution(G2)
plt.savefig("village_hist.pdf")

G1_LCC=max([G1.subgraph(c).copy() for c in nx.connected_components(G1)], key=len)
G2_LCC=max([G2.subgraph(c).copy() for c in nx.connected_components(G2)], key=len)

plt.figure()
nx.draw(G1_LCC, node_color="red", edge_color="grey", node_size=20)
plt.savefig("village1.pdf")

plt.figure()
nx.draw(G2_LCC, node_color="green", edge_color="grey", node_size=20)
plt.savefig("village2.pdf")