import networkx as nx
import dwave_networkx as dnx
import dimod
import matplotlib.pyplot as plt

from dwave.system.samplers import DWaveSampler
from dwave.system.composites import EmbeddingComposite

sampler=EmbeddingComposite(DWaveSampler(profile='cdl'))

G=nx.gnm_random_graph(12,25)
cut = dnx.maximum_cut(G, sampler, num_reads=50)

print('Size of the nodes, for maximum edges cut',len(cut))
print('The nodes, for maximum edges cut', cut)

subG=G.subgraph(cut)
notG=list(set(G.nodes())-set(cut))
other_subG=G.subgraph(notG)
pos=nx.circular_layout(G)
plt.figure()
nx.draw(G,pos=pos)
nx.draw(subG, pos=pos)
nx.draw(other_subG, pos=pos, node_color='b')
plt.show()
