#Per ogni richiesta che segue mostrare il grafico per i pianeti extrasolari e per quelli del Sistema Solore (opportunamente identificati).
#Creare un secondo script python che:
#1 - legga il file ExoplanetsPars_2025.csv e crei il DataFrame pandas corrispondente;
#suggerimento: usare l'opzione comment='#'
#2 - stampi il nome delle colonne del DataFrame;
#3 - stampi un estratto del contenuto del DataFrame;
#4 - produca un grafico con assi logaritmici della massa del pianeta in funzione del periodo orbitale;
#suggerimento: usare pyplot.scatter;
#5 - produca un grafico con assi logaritmici della grandezza in funzione del periodo orbitale;R_max: Orbit Semi-Major Axis e m_star: Stellar Mass
#6 - produca un grafico con assi logaritmici della massa del pianeta in funzione del periodo orbitale distinguendo gli esopianeti per metodo di scoperta (Transit o Radial Velocity) con la corrispondente legenda (gli altri tipi di esopianeti non vanno considerate nel grafico);
#suggerimento: usare .loc per la serezione dei valori nel DataFrame;
#suggerimento: usare l'opzione alpha per la trasparenza;
#7 - produca l'istogramma sovrapposto della massa del pianeta distinguendo gli esopianeti per metodo di scoperta (Transit o Radial Velocity) con la corrispondente legenda con la relativa legenda;
#suggerimento: usare pyplot.hist definendo lo stesso numero di bin e lo stesso intervallo per l'asse x;
#suggerimento: usare l'opzione alpha per la trasparenza;
#8 - produca un grafico analogo al precedente per il logaritmo in base 10 della massa del pianeta.

import pandas as pd
import matplotlib.pyplot as plt
import sys,os
import numpy as np
#1
exodf = pd.read_csv('ExoplanetsPars_2025.csv', comment='#')
#parametri Sistema Solare
ss_orbper  = np.array( [ 88, 225, 365, 687, 4333, 10759, 30687, 60190])
ss_orbsmax = np.array( [ 0.47, 0.73, 1.02, 1.67, 5.45, 10.07, 20.09, 30.32])
ss_bmasse = np.array( [ 0.06, 0.82, 1.0, 0.11, 317.89,  95.17, 14.56, 17.24, ] )
ss_bmassj = ss_bmasse/317.89
#2
"""print('Colonne:', exodf.columns)"""
#3
"""
parz_df = exodf.head
print(parz_df)
"""
#4 
r"""
fig, ax = plt.subplots(figsize=(12,6))
plt.scatter(exodf['pl_orbper'], exodf['pl_bmassj'], alpha=0.3, color='yellow', label='Esopianeti')
plt.scatter(ss_orbper, ss_bmassj, color='slategray', alpha=0.3, label='Sistema Solare')
plt.xlabel('Periodo Orbitale [giorni]', fontsize=16)
plt.ylabel(r'Massa del Pianeta [$m_J$]', fontsize=16)
plt.xscale('log')
plt.yscale('log')
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.legend(fontsize=16)
#plt.savefig('Exoplanets_ScatterPlot.pdf')
#plt.savefig('Exoplanets_ScatterPlot.png')
plt.show()
"""
#5
r"""
fig, ax = plt.subplots(figsize=(12,6))
plt.scatter(exodf['pl_orbper'],(exodf['pl_orbsmax']**2)/exodf['st_mass'], color='yellow', label='Esopianeti')
plt.scatter(ss_orbper, ss_orbsmax**2/ss_bmasse, color='slategray', label='Sistema Solare')
plt.xlabel('Periodo Orbitale [giorni]', fontsize=16)
plt.ylabel(r'$R_{max}^2/m_{\star}$ [$m_{\odot}^2/days$]', fontsize=16)
plt.xscale('log')
plt.yscale('log')
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.legend(fontsize=14)
#plt.savefig('Exoplanets_ScatterPlot_StMass.pdf')
#plt.savefig('Exoplanets_ScatterPlot_StMass.png')
plt.show()
"""
#6
r"""
fig, ax = plt.subplots(figsize=(12,6))
plt.scatter(exodf.loc[exodf['discoverymethod']=='Transit', 'pl_orbper'], exodf.loc[exodf['discoverymethod']=='Transit', 'pl_bmassj'], alpha=0.3, color='orange', label='Transit')
plt.scatter(exodf.loc[exodf['discoverymethod']=='Radial Velocity', 'pl_orbper'], exodf.loc[exodf['discoverymethod']=='Radial Velocity', 'pl_bmassj'], alpha=0.3, color='green', label='Radial Velocity')
plt.scatter(ss_orbper, ss_bmassj, color='slategray', label='Sistema Solare')
plt.xlabel(r'Periodo Orbitale [giorni]', fontsize=16)
plt.ylabel(r'Massa del Pianeta [$m_J$]', fontsize=16)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.xscale('log')
plt.yscale('log')
plt.legend(fontsize=14)
#plt.savefig('Exoplanets_ScatterPlot_Selezione.pdf')
#plt.savefig('Exoplanets_ScatterPlot_Selezione.png')
plt.show()
"""
#7

