figura = input("Ieraksti kādu figūru tu vēlies aprēķināt.\nizvēles ir: rinķis, trijstūris, taisnleņķa trijsturis,\nkvadrāts, taisnstūris, rombs, trapece:")
P_vai_S = input("Ko tu vēlies šai figūrai aprēķināt? Ieraksti \"perimetrs\" vai arī \"laukums\"")

if figura == "rinķis" or "Rinķis":
    if P_vai_S == "perimetrs":
        radiuss = float(input("Ievadi rinķa rādiusu (pi = 3.14): "))
        print("Rinķa perimetrs ir =", 2*3.14*radiuss)
    else:
        radiuss = float(input("Ievadi rinķa rādiusu (pi = 3.14): "))
        print("Rinķa laukums ir =",3.14 * radiuss^2)
