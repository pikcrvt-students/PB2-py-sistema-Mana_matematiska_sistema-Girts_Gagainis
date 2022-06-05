from asyncore import read

path = "C:\\Users\\girts\\Desktop\\Programmēšanas matemātikas darbs\\vardi_un_rezultati.txt"
fails = open(path, "r+", encoding="utf-8")

vārds = input("Ievadi savu vārdu: ")

print(fails.read())
