#Creare uno script python che combini:
#il grafico del punto 2.6 mostrando direttamente il logaritmo in base 10 dei valori invece di usare la scala logaritmica per gli assi,
#l'istogramma dei punti 2.8,
#un istogramma simile a quello del punto 2.8 ma per il periodo orbitale, in un'unica immagine come in figura e salvi il risultato in un file png e in un file pdf.

#la parte iniziale è del file exoplanets.py, questa è l'aggiunta opzionale
# Creo riquadro figura
fig = plt.figure(figsize=(12,11))

# creo griglia 2x2 per subplot con asse X in comune per le colonne e asse Y inb comune per le righe 
gs = fig.add_gridspec(2, 2, hspace=0, wspace=0)
ax = gs.subplots( sharex='col', sharey='row')

ax[1,0].scatter( np.log10(exodf.loc[exodf['discoverymethod']=='Transit',         'pl_orbper']),
                 np.log10(exodf.loc[exodf['discoverymethod']=='Transit',         'pl_bmassj']), color='limegreen',  alpha=0.3, label='Transit')
ax[1,0].scatter( np.log10(exodf.loc[exodf['discoverymethod']=='Radial Velocity', 'pl_orbper']),
                 np.log10(exodf.loc[exodf['discoverymethod']=='Radial Velocity', 'pl_bmassj']), color='darkorange', alpha=0.3, label='Radial Velocity')
ax[1,0].scatter(np.log10(ss_orbper), np.log10(ss_bmassj), color='slategray', label='Solar System')

ax[1,0].tick_params(axis='both', which='major', labelsize=14)
ax[1,0].set_xlabel('log(Period [days])',         fontsize=16)
ax[1,0].set_ylabel(r'log(Planet Mass [$m_J$])',  fontsize=16)
ax[1,0].legend(fontsize=16)


# Istogramma Periodo
ax[0,0].hist( np.log10(exodf.loc[exodf['discoverymethod']=='Transit', 'pl_orbper']),
              bins=50, range=(-2, 5), color='limegreen',  alpha=0.5, label='Transit')

ax[0,0].hist( np.log10(exodf.loc[exodf['discoverymethod']=='Radial Velocity', 'pl_orbper']),
              bins=50, range=(-2, 5), color='darkorange',  alpha=0.5, label='Radial Velocity')
ax[0,0].tick_params(axis='both', which='major', labelsize=14)
ax[0,0].set_ylabel(r'Number of planets',        fontsize=16)
ax[0,0].legend(fontsize=16)


# Istogramma Massa pianeta
ax[1,1].hist( np.log10(exodf.loc[exodf['discoverymethod']=='Transit', 'pl_bmassj']),
              bins=50, range=(-4, 4), color='limegreen',  alpha=0.5, orientation='horizontal', label='Transit')

ax[1,1].hist( np.log10(exodf.loc[exodf['discoverymethod']=='Radial Velocity', 'pl_bmassj']),
              bins=50, range=(-4, 4), color='darkorange',  alpha=0.5, orientation='horizontal', label='Radial Velocity')

ax[1,1].tick_params(axis='both', which='major', labelsize=14)
ax[1,1].set_xlabel( 'Number of planets',        fontsize=16)
ax[1,1].legend(fontsize=16)

# Rimuovo assi per riquadro non necessario
ax[0,1].axis('off')

plt.savefig('Exoplanets_Period_vs_Mass_Detection.pdf')
plt.savefig('Exoplanets_Period_vs_Mass_Detection.png')
plt.show()
