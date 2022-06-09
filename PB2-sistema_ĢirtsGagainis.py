import random
import math
from tkinter import Y

print("Izvēlies kādu no pieejamajām tēmām: kvadrātvienādojums_teorija(), kvadrātvienādojums_uzdevumi(), kvadrātvienādojums_pd().")

def kvadrātvienādojums_teorija():
    print("Kvadrātvienādojuma teorija!\n\n")
    print("Par kvadrātvienādojumu sauc vienādojumu, kurš ir dots (vai to var pārveidot) formā ax2+bx+c=0, kur a, b, c ir reāli skaitļi, turklāt a≠0, bet x - mainīgais.\nVispārīgā kvadrātvienādojuma ax^2+bx+c=0 saknes aprēķina, izmantojot formulu: D=b^2−4ac, un saknes ar x1 = (-b + sqrt(D))/2*a) un x2 = (-b - sqrt(D))/2*a)\n\n")
    print("Saknes arī var aprēķināt ar Vjeta teorēmu. Parasti Vjeta teorēmu lieto reducētam kvadrātvienādojumam, t.i., ja koeficients a = 1.\nax^2 + bx + c = 0        x1 * x2 = c     un   x1 + x2 = -b")

def kvadrātvienādojums_uzdevumi():
    #1. uzd
    atbilde1 = int(input("1. uzdevums: Kāds ir diskriminants vienādojumam X^2 + 12X + 7 = 0?: "))
    if atbilde1 == 116:
        print("Pareiza atbilde! +1 punkts!\n")
    else: 
        print("Nepareizi!\n")

    #2. uzd
    print("2. Uzdevums: Kādas ir šī piemēra saknes? 5X^2 - 16X + 3 = 0")
    atbilde2 = float(input("1. sakne ir: "))
    atbilde3 = float(input("2. sakne ir: "))
    if atbilde2 == 3 or atbilde2 == 0.2 and atbilde3 == 0.2 or atbilde3 == 3:
        print("Pareiza atbilde! +1 punkts!\n")
    else: 
        print("Nepareizi!\n")
    
    #3 uzd
    print("3. Uzdevums: Kādas ir šī piemēra saknes? X^2 - 14X + 40 = 0")
    atbilde4 = float(input("1. sakne ir: "))
    atbilde5 = float(input("2. sakne ir: "))
    if atbilde4 == 10 or atbilde4 == 4 and atbilde5 == 4 or atbilde5 == 10:
        print("Pareiza atbilde! +1 punkts!\n")
    else: 
        print("Nepareizi!\n")
    
    #4 uzd
    print("4. Uzdevums: Kādas ir šī piemēra BX un C vērtības? AX^2 - BX + C = 0, ja saknes ir 5 un -3?")
    atbilde6 = float(input("BX vērtība ir: "))
    atbilde7 = float(input("C vērtība ir: "))
    if atbilde6 == -2 and atbilde7 == -5:
        print("Pareiza atbilde! +1 punkts!\n")
    else: 
        print("Nepareizi!\n")

    #5 uzd 
    print("5. Uzdevums: Kāda ir šī piemēra saknes? X^2 - 5X + 6 = 0")
    atbilde8 = float(input("1. sakne ir: "))
    atbilde9 = float(input("2. sakne ir: "))
    if atbilde8 == 2 or atbilde8 == 3 and atbilde9 == 2 or atbilde9 == 3:
        print("Pareiza atbilde! +1 punkts!\n")
    else: 
        print("Nepareizi!\n")




import random
import math

def kvadrātvienādojums_pd():
    username = input("Ievadi savu vārdu: ")
    vardi_punkti = ["Rezultāti:"]
    print("Kvadrātvienādojuma pārbaudes darbs!\nPārbaudes darbs sastāvēs no 10 dažādiem uzdevumiem, kuri mainīsies katru reizi.\n")
    print("Saknes noapaļo līdz diviem skaitļiem aiz komata")
    max_punkti = 10
    user_punkti = 0
    a_vertibas = [0] * 10
    b_vertibas = [0] * 10
    c_vertibas = [0] * 10
    

    for i in range(10):
        print(i+1, ". uzdevums:")
        a_vertibas[i] = random.randint(1, 3)
        b_vertibas[i] = random.randint(5, 15)
        c_vertibas[i] = random.randint(-5, 10)
        print("Ievadi šī vienādojuma saknes, ja\nA =",a_vertibas[i],"\nB =",b_vertibas[i], "\nC =",c_vertibas[i])
        diskriminants = (math.pow(b_vertibas[i],2)) - (4*a_vertibas[i]*c_vertibas[i])

        if diskriminants > 0:
            augša1 = -b_vertibas[i] + math.sqrt(diskriminants)
            leja1 = 2 * a_vertibas[i]
            sakne1 = augša1 / leja1
            augša2 = -b_vertibas[i] - math.sqrt(diskriminants)
            leja2 = 2 * a_vertibas[i]
            sakne2 = augša2 / leja2
         
            sakne1 = round(sakne1, 2)
            sakne2 = round(sakne2, 2)
            ievadita_sakne1 = float(input("Ievadi pirmās saknes vērtību: "))
            ievadita_sakne2 = float(input("Ievadi otrās saknes vērtību: "))
            
            if ievadita_sakne1 == sakne1 or ievadita_sakne1 == sakne2 and ievadita_sakne2 == sakne2 or ievadita_sakne2 == sakne1:
                print("Pareizi! +1 punkts\n")
                user_punkti += 1
            else:
                print("Nepareizi! +0 punkti")



        elif diskriminants == 0: 
            sakne1 = sakne1 = (-b_vertibas[i]-math.sqrt(diskriminants))/(2 * a_vertibas[i])
            ievadita_sakne1 = float(input("Ievadi pirmās saknes vērtību: "))
            if ievadita_sakne1 == sakne1:
                print("Pareizi! +1 punkts\n")
                user_punkti += 1
            else:
                print("Nepareizi! +0 punkti")
        
        else:
            print("Diskriminanta sakne ir 0, nākamais piemērs")
        
    print("Tu ieguvi:", user_punkti, "tavs vārds: ", username)
    
    rezultatu_path = input("Ievadi rezultātu faila lokācijU (C:..faila_nosaukums.txt): ")
    rezultati = open(rezultatu_path, "a")
    ko_ierakstit = [username, " ieguva ", user_punkti, "punktus"]
    rezultati.write("\n")
    rezultati.write(str(ko_ierakstit))
    rezultati.close
