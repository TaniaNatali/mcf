#Sviluppare uno script python che
#Crei una lista con i nomi dei giorni della settimana
#Crei una lista col nome dei giorni della settimana per tutto il mese di ottobre 2025
#Crei un dizionario che metta in relazione il giorno del mese di ottobre 2025 con il giorno della settimana
#Stampi la correlazione fra giorno del mese e della settimana a sc 

lista_settimana=['lunedì','martedì','mercoledì','giovedì','venerdì','sabato','domenica']
lista_ottobre=lista_settimana[2:]+lista_settimana*3+lista_settimana[:5]
print('I giorni di ottobre sono: ',lista_ottobre)
oct_dict={}
print('Il calendario di ottobre 2025 è: ')
for i in range(len(lista_ottobre):
	oct_dict[i+1]=lista_ottobre[i]
	#oppure metodo base: oct_dict.update({i+1: lista_ottobre[1]})
"""oppure con List Comprehension: oct_dict={i+1:lista_ottobre[i] for i range(len(lista_ottobre))}
stampa a schermo il dizionario 
for k in oct_dict:
	print('||{:5d}{:.>36}{:>12}'.format(k, oct_dict[k], '||')) """
print(oct_dict)
n=input('Che giorno della settimana è il ')
g=int(n)
print('Il', g, 'ottobre è',oct_dict[g])

