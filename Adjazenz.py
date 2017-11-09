
def Graphentheori(V,E):
    return filter(lambda x: x[0]==E,V)

V = ['A','B','C','D','E','E','V','B','C']




def Graphen(V,E):
    Total =[]
    for k,v in enumerate(V):
        if v == E:
            Total.append(k)
    return Total





a = [1,0,0,1]
b = [0,1,1,1]
c  =[1,1,1,1]
d = [1,1,1,1]

lst = [a,b,c,d]



def Umwandlung():

    Total = []
    Total1 = []
    Total2 = []
    Total3 = []

    for c,v in enumerate(lst):

        Total.append(v[0])
        Total1.append(v[1])
        Total2.append(v[2])
        Total3.append(v[3])
        c = [Total, Total1, Total2, Total3]
    return c

r = Umwandlung()
def A(r):
    Total = []
    for i,k in enumerate(r[0]):
        if k == 0:
            pass
        else:
            if i==0:
                Total.append('A')
            elif i==1:
                Total.append('B')
            elif i ==2:
                Total.append('C')
            elif i ==3:
                Total.append('D')


    return Total
def B(r):
    Total = []
    for i,k in enumerate(r[1]):
        if k == 0:
            pass
        else:
            if i==0:
                Total.append('A')
            elif i==1:
                Total.append('B')
            elif i ==2:
                Total.append('C')
            elif i ==3:
                Total.append('D')


    return Total
def C(r):
    Total = []
    for i,k in enumerate(r[2]):
        if k == 0:
            pass
        else:
            if i==0:
                Total.append('A')
            elif i==1:
                Total.append('B')
            elif i ==2:
                Total.append('C')
            elif i ==3:
                Total.append('D')


    return Total
def D(r):
    Total = []
    for i,k in enumerate(r[3]):
        if k == 0:
            pass
        else:
            if i==0:
                Total.append('A')
            elif i==1:
                Total.append('B')
            elif i ==2:
                Total.append('C')
            elif i ==3:
                Total.append('D')


    return Total

def Add():
    Total = []
    Total.extend(A(r))
    Total.extend(B(r))
    Total.extend(C(r))
    Total.extend(D(r))
    return Total


print ('Ausgangsgrad ist', Graphen(V,'E')) # Gibt aus den Index von E in V.
print (Add()) #Umwandelt die Matrize in einer Adjazenzliste.
print (Graphen(Add(),'D')) # Findet den Index von D in der Liste Add.
