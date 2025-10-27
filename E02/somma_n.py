#Creare uno script che:
#chieda in input un numero intero n
#stampi a schermo la somma dei primi n numeri naturali

n=input('Scrivi un numero intero: ')
num=int(n)
somma=0
for i in range(num+1):
    somma=somma+i
print('La somma dei primi ', n, ' numeri naturali è ', somma)
