import os
print("ciao questo è un programma per pingare un ip/dns \n")
print("inserisci l'host... ")
x = str(input())
print("\nora scegli quante volte vuoi far ripetere il ping... ")
y = int(input())
if x=="":
    pass
else:
    for i in range(y):
        os.system("ping "+ x)
