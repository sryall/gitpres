# Example for the group

import matplotlib.pyplot as plt
import sys

script_location = '/home/anderson/Documents/UW_AM_Research' + \
        '/Code/GEMFPython'

sys.path.append(script_location)

from GEMFPy import *

# Will
# Genrate graph
G=nx.random_geometric_graph(100,0.151)
pos=nx.get_node_attributes(G,'pos')

# find node near center (0.5,0.5)
dmin=1
ncenter=0
for n in pos:
    x,y=pos[n]
    d=(x-0.5)**2+(y-0.5)**2
    if d<dmin:
        ncenter=n
        dmin=d

# Mehrshad
# color by path length from node near center
p=nx.single_source_shortest_path_length(G,ncenter)

# Population
N = G.number_of_nodes()

# Rui
# Parameters and model
beta = 1.2; delta = 2;
Para = Para_SIS(delta,beta)

# initial conditions
x0 = np.zeros(N)
x0 = Initial_Cond_Gen(N, Para[1][0], 2, x0)

#sameed
# Sim variables
Net = NetCmbn([MyNet(G)])
StopCond = ['RunTime', 10]

# Simulation
t, f = MonteCarlo(Net, Para,  StopCond, 1, 3, .1, 20, N, x_init = np.zeros(N))

# Dania
# plotting
fig = plt.figure()
ax0 =fig.add_subplot(211)
ax0 = nx.draw_networkx(G, pos, node_size =200)

ax1 = fig.add_subplot(212)
ax1.plot(t,f[0,:],'r',label='Susceptible')
ax1.plot(t,f[1,:],'b',label='Infected')

# Stephanie
ax1.set_xlabel('Time (day)')
ax1.set_ylabel('Fraction of Population')
plt.show(block=True)

