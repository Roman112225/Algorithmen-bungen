import random
from operator import itemgetter

Farben = {'Karo':4,'Herz':3,'Pik':2,'Kreuz':1}
Karten = {'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'Bube':11,'Dame':12,'Koenig':13,'Ass':14}

def Stappel():
    l=[]
    for Farbe in Farben:
        for Karte in Karten:
            if len(l) <36:
                Card = (Farbe, Karte)
                if Card not in l:
                    l.append(Card)
    return l
c = Stappel()

print c


def HalloWelt():
    Liste = []
    for i in c:
        Total = []
        for key,value in Farben.iteritems():
            if i[0]==key:
                Total.append(value)
        for key,value in Karten.iteritems():
            if i[1]==key:
                Total.append(value)
        Liste.append(Total) ##Hab identifiziert den Wert dieser Karte
    return Liste
s = HalloWelt()


def Wert(s):
    Total = []
    for i in s:
        Total.append(i[0]+i[1]) ##Den Wert von Farbe und Karte berechnet
    return Total


print Wert(s)

q= zip(c,Wert(s))

def Ordnung(j):
    Total = []
    for i in j:
        for l in i:
            if l[0]>l[1]:
                l[0]>l[1]


c = ['Jo','Wie','Gehts']
d = ['Konnte','was','besseres']

print sorted(zip(c,d),key = lambda x :(x[1], len(x[1])),reverse=True)

print len(q)
print sorted(q,key=lambda x:(x[1], len  (x[0])),reverse=True)
