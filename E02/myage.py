#Creare uno script Python che:
#chieda in input la vostra data di nascita;
#calcoli la vostra età in anni, giorni e secondi;
#stampi a schermo i risultati con stringhe formattatate in modo che appaiano incolonnati; per svolgere questa parte è necessario familiarizzare con il modulo datetime

import sys,os
from datetime import datetime, timedelta
nascita = input('Inserisci la tua data di nascita g-m-a ore:minuti:secondi: ')
# definisco data da stringa formattata giorno-mese-anno
mybdaydate = datetime.strptime(nascita, "%d-%m-%Y %H:%M:%S")
datenow = datetime.now()
print('La data attuale è: {:d}-{:d}-{:d}'.format( datenow.day, datenow.month, datenow.year))
#calcolo l'età facendo la differenza degli anni
età_years=datenow.year-mybdaydate.year
if datenow.month < mybdaydate.month or (datenow.month == mybdaydate.month and datenow.day < mybdaydate.day):
	età_years-=1
#calcolo differenza temporale con datetime
datediff = datenow-mybdaydate
datediff_sec = datediff.total_seconds()
età_secs=int(datediff_sec)
età_hours=int(datediff_sec/(60*60))
#print('Data di nascita  {:02d}-{:02d}-{:d}'.format( mybdaydate.day, mybdaydate.month, mybdaydate.year))
#print('Data attuale     {:02d}-{:02d}-{:d}'.format( datenow.day,    datenow.month,    datenow.year))
print('Età    [anni]: {:>12d}'.format(età_years))
print('Età     [ore]: {:>12d} - {:>6d} khr'.format(età_hours, int(età_hours/1000)))
print('Età [secondi]: {:>12d} - {:>6d} Ms'.format(età_secs,   int(età_secs/1e6)  ))

