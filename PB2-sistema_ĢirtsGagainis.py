def kvadrātvienādojums():
    gala_punkti = 0
    print("Teorija: Par kvadrātvienādojumu sauc vienādojumu, kurš ir dots (vai to var pārveidot) formā ax2+bx+c=0, kur a, b, c ir reāli skaitļi, turklāt a≠0, bet x - mainīgais.")
    print("Vispārīgā kvadrātvienādojuma ax^2+bx+c=0 saknes aprēķina, izmantojot formulu: D=b^2−4ac, un saknes ar x1 = (-b + sqrt(D))/2*a) un x2 = (-b - sqrt(D))/2*a)\n")

    atbilde1 = int(input("1. uzdevums: Kāds ir diskriminants vienādojumam X^2 + 12X + 7 = 0?: "))
    if atbilde1 == 116:
        print("Pareiza atbilde! +1 punkts!\n")
        gala_punkti += 1
    else: 
        print("Nepareizi!\n")
        
    print("Kādas ir šī piemēra saknes? 5X^2 - 16X + 3 = 0")
    atbilde2 = float(input("1. sakne ir: "))
    atbilde3 = float(input("2. sakne ir: "))
    if atbilde2 == 3 or atbilde2 == 0.2 and atbilde3 == 0.2 or atbilde3 == 3:
        print("Pareiza atbilde! +1 punkts!\n")
        gala_punkti += 1
    else: 
        print("Nepareizi!\n")
    



    
kvadrātvienādojums()

