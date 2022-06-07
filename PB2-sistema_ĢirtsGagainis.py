from random import randint
from github import Github
print("Izvēlies kādu no pieejamajām tēmām: kvadrātvienādojums(), pitagora_teorēma()")
def kvadrātvienādojums():
    gala_punkti = 0
    print("Teorija: Par kvadrātvienādojumu sauc vienādojumu, kurš ir dots (vai to var pārveidot) formā ax2+bx+c=0, kur a, b, c ir reāli skaitļi, turklāt a≠0, bet x - mainīgais.")
    print("Vispārīgā kvadrātvienādojuma ax^2+bx+c=0 saknes aprēķina, izmantojot formulu: D=b^2−4ac, un saknes ar x1 = (-b + sqrt(D))/2*a) un x2 = (-b - sqrt(D))/2*a)\n")

    #1. uzd
    atbilde1 = int(input("1. uzdevums: Kāds ir diskriminants vienādojumam X^2 + 12X + 7 = 0?: "))
    if atbilde1 == 116:
        print("Pareiza atbilde! +1 punkts!\n")
        gala_punkti += 1
    else: 
        print("Nepareizi!\n")
    #2. uzd
    print("2. Uzdevums: Kādas ir šī piemēra saknes? 5X^2 - 16X + 3 = 0")
    atbilde2 = float(input("1. sakne ir: "))
    atbilde3 = float(input("2. sakne ir: "))
    if atbilde2 == 3 or atbilde2 == 0.2 and atbilde3 == 0.2 or atbilde3 == 3:
        print("Pareiza atbilde! +1 punkts!\n")
        gala_punkti += 1
    else: 
        print("Nepareizi!\n")
    

    print("Teorija: Var arī pielietot Vjeta teorēmu, lai noteiktu saknes.\n Reducēta kvadrātvienādojuma sakņu reizinājums ir vienāds ar brīvo locekli, bet sakņu summa ir vienāda ar lineārā locekļa koeficientam pretējo skaitli.")
    print("x1 * x2 = c un x1 + x2 = -b\n")
    
    
    #3 uzd
    print("3. Uzdevums: Kādas ir šī piemēra saknes? X^2 - 14X + 40 = 0")
    atbilde4 = float(input("1. sakne ir: "))
    atbilde5 = float(input("2. sakne ir: "))
    if atbilde4 == 10 or atbilde4 == 4 and atbilde5 == 4 or atbilde5 == 10:
        print("Pareiza atbilde! +1 punkts!\n")
        gala_punkti += 1
    else: 
        print("Nepareizi!\n")
    
    #4 uzd
    print("4. Uzdevums: Kādas ir šī piemēra BX un C vērtības? AX^2 - BX + C = 0, ja saknes ir 5 un -3?")
    atbilde6 = float(input("BX vērtība ir: "))
    atbilde7 = float(input("C vērtība ir: "))
    if atbilde6 == -2 and atbilde7 == -5:
        print("Pareiza atbilde! +1 punkts!\n")
        gala_punkti += 1
    else: 
        print("Nepareizi!\n")

    #5 uzd 
    print("5. Uzdevums: Kāda ir šī piemēra saknes? X^2 - 5X + 6 = 0")
    atbilde8 = float(input("1. sakne ir: "))
    atbilde9 = float(input("2. sakne ir: "))
    if atbilde8 == 2 or atbilde8 == 3 and atbilde9 == 2 or atbilde9 == 3:
        print("Pareiza atbilde! +1 punkts!\n")
        gala_punkti += 1
    else: 
        print("Nepareizi!\n")
    



    print("Tev ir",gala_punkti, "punkti!")
kvadrātvienādojums()

