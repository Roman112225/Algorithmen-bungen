E = {('SFX','TXL'),('FRA','CGN'),('FRA','MUC'),('FRA','STR'),('CGN','FRA'),('STR','FRA'),('TXL','SFX'),('CGN','PAD'),('PAD','KEL'),('MUC','KEL'),('KEL','STR')   }


def Nachbar(V,E):
    Total = []
    Que = []
    for i in E:

        for j in i:
            if j == V:
                Total.append(i)

    for i in Total:
        for a in i:
            if a != V:
                if a not in Que:

                    Que.append(a)

    return Que


def Si(V,E):
    Liste = []
    Besucht = []
    J = []
    K = []
    Liste.extend(Nachbar(V, E))
    for i in Liste:
        if i not in Besucht:
            J.extend(Nachbar(i,E))
            Besucht.append(i)
            for x in J:
                if x not in Besucht:
                    Besucht.append(x)
                    K.extend(Nachbar(x,E))
    return Besucht


print (Si('SFX',E))
