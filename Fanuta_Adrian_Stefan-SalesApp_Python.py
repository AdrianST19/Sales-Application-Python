# Se dau în mii lei vânzările valorice pentru un număr de m magazine pe o perioadă de n zile. Să se descrie prin schemă logică și prin instrucțiuni în pseudocod sau
# prin instrucțiunile unui limbaj de programare, un algoritm eficient pentru rezolvarea următoarelor cerințe referitoare la o firmă cu aceste magazine:

# 1.Să se preia în memoria internă valoarea vânzărilor pentru fiecare dintre cele m magazine în fiecare zi (din cele n zile).
nr_magazine=int(input("Introduceti numarul de MAGAZINE: "))
nr_zile=int(input("Introduceti numarul de ZILE: "))
valoarea_vanzarilor=[]
i=0
while i<=nr_magazine-1:
    j=0
    rand=[]
    while j<=nr_zile-1:
        nr=float(input("Introduceti valoarea vanzarilor pentru magazinul "+str(i+1)+" din ziua "+str(j+1)+": "))
        rand.append(nr)
        j=j+1
    valoarea_vanzarilor.append(rand)
    i=i+1
# 2.Să se calculeze valoarea totală rotunjită la milioane lei, cu o zecimală, a vânzărilor pentru fiecare dintre cele m magazine pentru cele n zile și 
# cea a vânzărilor pe fiecare zi (din cele n zile) a celor m magazine. 
def sum1(input):
    for i in range(0, nr_magazine):  
        sumLinii = 0;  
        for j in range(0, nr_zile):  
            sumLinii = sumLinii + valoarea_vanzarilor[i][j];  
            round(sumLinii)
            sumLinii1=sumLinii *10000
        print("Vânzările pentru magazinul " + str(i+1) +": " + str(sumLinii1),"lei"); 
    
def sum2(input):
    for i in range(0, nr_magazine):  
        sumColoana = 0;  
        for j in range(0, nr_zile):  
            sumColoana = sumColoana + valoarea_vanzarilor[j][i];  
            round(sumColoana)
            sumColoana1=sumColoana *10000
            print("Vânzările pentru ziua " + str(i+1) +": " + str(sumColoana1),"lei");  

# 3.Să se determine valoarea minimă rotunjită la un număr întreg a vânzărilor pentru fiecare magazin și ziua (zilele) în care s-a(u) realizat.
def ValoareaMinimaMagazin(matrice, coloana, linie): 
    for i in range(nr_magazine): 
        print("Cea mai mica valoare vanduta in magazinul "+str(i+1)+" ziua "+str(j+1)+": ",round(min(valoarea_vanzarilor[i])),"lei")
n= nr_magazine
m = nr_zile
mat= valoarea_vanzarilor

# 4.Să se determine valoarea minimă rotunjită la un număr întreg a vânzărilor realizate pentru fiecare zi și magazinul/ele în care s-a realizat.
def ValoareaMinimaZile(matrice, linie, coloana): 
    for i in range(nr_magazine): 
        minm = matrice[0][i]
        for j in range(nr_zile): 
            if matrice[j][i] < minm: 
                minm = matrice[j][i] 
        print("Cea mai mica valoare vanduta in ziua "+str(j+1)+" magazinul "+str(i+1)+": ",round(minm),"lei")

# 5.Idem 3,4 dar cu valoarea maximă rotunjită la un număr întreg.
def ValoareaMaximaMagazin(matrice, linie, coloana): 
    for i in range(nr_magazine): 
        maxm = matrice[0][i]
        for j in range(nr_zile): 
            if matrice[j][i] > maxm: 
                maxm = matrice[i][j] 
        print("Cea mai mare valoare vanduta in magazinul "+str(i+1)+" ziua "+str(j+1)+": ",round(maxm), "lei")

def ValoareaMaximaZile(matrice, linie, coloana): 
    for i in range(nr_magazine): 
        maxm = matrice[0][i]
        for j in range(nr_zile): 
            if matrice[j][i] > maxm: 
                maxm = matrice[j][i] 
        print("Cea mai mare valoare vanduta in ziua "+str(j)+" magazinul "+str(i+1)+": ",round(maxm), "lei")

# 6. Să se determinte rotunjite la un număr întreg valorile vânzării minime si maxime, din toată aceasta perioadă de vânzări (matrice) și 
# să se specifice ce magazine(e) a(u) realizat-o și în ce zi(le).

mymin = min([min(i) for i in valoarea_vanzarilor])
mymax = max([max(i) for i in valoarea_vanzarilor])

# 7. Să se determine valoarea totală rotunjită la milioane lei, cu o zecimală a vânzărilor din toate cele m magazine în perioada de n zile.
def sum3(input):
    sum = 0
    for nr_magazine in range (len(input)):
        for nr_zile in range(len(input[0])):
            sum = sum + input[nr_magazine][nr_zile]
    sum=sum*10000
    return sum 

# 8. Să se afișeze la sfârșit toate rezultatele.

# Cerinta 1
print("CERINTA 1")
i=0
while i<=nr_magazine-1:
    j=0
    while j<=nr_zile-1:
        print(valoarea_vanzarilor[i][j], end=" ")
        j=j+1    
    print()
    i=i+1
# Cerinta 2
print("CERINTA 2")
print(sum1(valoarea_vanzarilor))
print(sum2(valoarea_vanzarilor))
# Cerinta 3
print("CERINTA 3")
print(ValoareaMinimaMagazin(mat, m, n))
# Cerinta 4
print("CERINTA 4")
print(ValoareaMinimaZile(mat, n, m))
# Cerinta 5
print("CERINTA 5")
print(ValoareaMaximaMagazin(mat, n, m))
print(ValoareaMaximaZile(mat, n, m))
# Cerinta 6
print("CERINTA 6")
print("Cea mai mica vanzare din aceasta perioada a fost de",round(mymin),"in magazinul", nr_magazine,"ziua",nr_zile)
print("Cea mai mare vanzare din aceasta perioada a fost de",round(mymax),"in magazinul", nr_magazine,"ziua",nr_zile)
# Cerinta 7
print("CERINTA 7")
print ("Valoarea totală a vânzărilor din toate cele m magazine în perioada de n zile este de",round(sum3(valoarea_vanzarilor)),".")