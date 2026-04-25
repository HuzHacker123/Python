Names = ["Huzefa","Rehan","Zahid","Ali","Hassan","Fuck",
         "Zainab","Ayesha","Fatima","Sana","Amir","Fuck",
         "Omar","Hassan","Zoya","Ibrahim","Fuck","Maryam",
         "Noor","Sara","Usman","Bilal","Khadija","Fuck",]

c = Names.count("Fuck")
print("There are",c,"Fucks in the list.")
for i in range(len(Names)):
    if Names[i] == "Fuck":
        Names[i] = "*" * len(Names[i])
print("The cuss word in the list have been censored.")
print(Names)
