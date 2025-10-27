#Creare uno script python che:
#1 - legga il file kplr010666592-2011240104155_slc.csv e crei il DataFrame pandas corrispondente;
#2 - stampi il nome delle colonne del DataFrame;
#3 - produca un grafico del flusso in funzione del tempo
# - suggerimento: usare pyplot.plot;
#4 - produca un grafico del flusso in funzione del tempo coi punti del grafico demarcati da un simbolo (no linea);
#suggerimento: usare pyplot.plot con opzione 'o' o equivalente;
#5 - produca un grafico del flusso in funzione del tempo con barre di errore e salvi il risultato in un file png e/o pdf;
#suggerimento: usare pyplot.errorbar;
#6 - produca un grafico simile al precedente selezionando un intervallo temporale attorno ad uno dei minimi;
#suggerimento: usare .loc per la serezione dei valori nel DataFrame;
#7 - produca un grafico come per il punto 5 ma con la selezione del punto 6 mostrata come riquadro.
#suggerimento: utilizzare inset_axes

import pandas as pd
import matplotlib.pyplot as plt
#1
df = pd.read_csv('dati_kepler.csv')
#2
"""print(df.columns)"""
#3
time_x=df['TIME']
flusso_y=df['PDCSAP_FLUX']
"""plt.plot(time_x, flusso_y, markersize=3, color='blue')
plt.xlabel('tempo')
plt.ylabel('flusso')
plt.show()"""
#4
"""plt.plot(time_x,flusso_y,'o', color='red')
plt.show()"""
#5
flusso_er=df['PDCSAP_FLUX_ERR']
"""plt.errorbar(time_x,flusso_y,yerr=flusso_er, fmt='o', markersize=3)
plt.xlabel('tempo')
plt.ylabel('flusso')
#plt.savefig("grafico_flusso_errore.pdf")
plt.show()"""
#6
df_min=df.loc[(df['TIME']<940.0) & (df['TIME']>939.0)]
"""plt.errorbar(df_min['TIME'], df_min['PDCSAP_FLUX'], yerr=df_min['PDCSAP_FLUX_ERR'], fmt='o', markersize=3)
plt.xlabel('tempo')
plt.ylabel('flusso')
plt.show()"""
#7
fig, ax = plt.subplots(figsize=(12,10))
ax.errorbar(time_x, flusso_y, yerr=flusso_er, fmt='o', markersize=3)
ax.set_xlabel('tempo')
ax.set_ylabel('flusso')
ins_ax = ax.inset_axes([0.8, 0.85, 0.20, 0.15]) 
ins_ax.errorbar(df_min['TIME'], df_min['PDCSAP_FLUX'], yerr=df_min['PDCSAP_FLUX_ERR'], fmt='o', markersize=3)
plt.show()




