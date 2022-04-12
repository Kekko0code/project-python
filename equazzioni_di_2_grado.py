import fractions
from functools import total_ordering
import math
import string

#in input a,b,c 

print(" questo programma riesce a risolvere una equazione di 2 grado da solo \n")
a = float(input("inserisci a : "))
b = float(input("inserisci b : "))
c = float(input("inserisci c : "))
#definire i tipi di equazioni

def completa():
    print("è una equazione completa ")
    delta = b*b-4*a*c
    rad_delta = math.sqrt(delta)
    dem_compl = 2*a
    xa1 = -b+rad_delta
    x1 = fractions.Fraction(xa1/dem_compl)
    xa2 = -b-rad_delta
    x2 = fractions.Fraction(xa2/dem_compl)
    print("x1 : ",x1,"\nx2 : ",x2)
    print("se vuoi calcolare il trinomio speciale di 2 grade scrivi s/n : ")
    risp = str(input())
    if risp == "s" or "s":
        trin = a*(x1)*(x2)
        print(trin)


def spuria():
    print("è una equazione spuria ")
    x1 = 0
    x2 = fractions.Fraction(-b/a)
    print("x1 : ",x1,"\nx2 : ",x2)

def pura():
    print("è una equazione pura ")
    frax1  = fractions.Fraction(-c/a)
    x1 = math.sqrt(frax1)
    if x1<0:
        x1 = x1 * +1
    else:
        x1 = x1 * -1
    frax2  = fractions.Fraction(-c/a)
    x2 = math.sqrt(frax2)
    if x2<0:
        x2 = x2 * -1
    else:
        x2 = x2 * +1
    print("x1 : ",x1,"\nx2 : ",x2)



def monomia():
    print("è una equazione monomia ")
    print("x1 : 0","\nx2 : 0")

    
def s_p():
    if a == 0:
        print("se a è uguale a 0 la s e p non è possibile ")
    else:
        s = fractions.Fraction(-b/a)
        p = fractions.Fraction(c/a)
        print("s : ",s,"p : ",p)


#capire che tipo di equazione di 2 grado è

if c==0 and b!=0 :
    spuria()
elif b==0 and c!=0:
    pura()
elif b==0 and c==0 and a!=0:
    monomia()
elif a==0 and b==0 and c==0:
    print("errore 404 a,b,c not faund")
else : 
    completa()

print("vuoi calcolare pure S e P ? s/n ")
risp = str(input())
if risp == "s" or "S":
    s_p()
else:
    pass
