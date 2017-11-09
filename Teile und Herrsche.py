# Algorithmen und Datenstrukturen
# Hausaufgabe 1 - Matrixmultiplikation
# Abgabedatum: 21.5.2017
#
# Gruppennummer: 60
# Gruppenmitglieder:
# - Arne Spieß
# - Roman Moraru

# Ausgabe der Matrix
def printMatrix(m):
    for line in m:
        print('|', end=' ');
        i = 0;
        for value in line:
            if (i > 0):
                print(' ', end='');
            print(value, end='');
            i = i + 1;
        print("|");

# Multiplikation der Matrix a und b nach Definition
def matMultDef(a, b):
	print('Parameter a:');
	printMatrix(a);
	print('Parameter b:');
	printMatrix(b);

	# Berechnung der Matrix c nach Definition
	r1 = a[0][0]*b[0][0]+a[0][1]*b[0][1];
	r2 = a[1][0]*b[1][0]+a[1][1]*b[1][1];
	r3 = a[0][0]*b[1][0]+a[0][1]*b[1][1];
	r4 = a[1][0]*b[0][0]+a[1][1]*b[0][1];
	result = [[r1,r2],[r3,r4]];

	print('Folgende Matrix wurde berechnet (Definition):');
	printMatrix(result);
	return;

# Multiplikation der Matrix a und b nach Divide and Conquer
def matMultDC(a, b):
	print("Parameter a:");
	printMatrix(a);
	print('Parameter b:');
	printMatrix(b);

	# Berechnung der Matrix c nach D&C
	r1 = a[0][0]*b[0][0]+a[0][1]*b[1][0];
	r2 = a[0][0]*b[0][1]+a[0][1]*b[1][1];
	r3 = a[1][0]*b[0][0]+a[1][1]*b[1][0];
	r4 = a[1][0]*b[0][1]+a[1][1]*b[1][1];
	result = [[r1,r2],[r3,r4]];

	print('Folgende Matrix wurde berechnet (Divide and Conquer):');
	printMatrix(result);
	return;

a = [[3,4],[6,9]];
b = [[1,5],[11,8]];
matMultDef(a,b);
print('----------------------------------------------------------------');
matMultDC(a,b);
