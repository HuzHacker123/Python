dict={"Aam":"mango", "Keela":"Banana", 
      "Amrut":"Guava", "Anar":"Pomegranate", 
      "Angoor":"Grapes", "Tarbooj":"Watermelon", 
      "Papita":"Papaya", "Santra":"Orange", "Seb":"Apple", 
      "Chiku":"Sapodilla", "Nashpati":"Pear", "Jamun":"Black Plum", 
      "Lichi":"Lychee", "Anjeer":"Fig", "Kharbooza":"Muskmelon"}
print("Welcome to Fruit Dictionary")
print("You can know the English names of fruits by entering their Hindi names")
a=input("Enter the Hindi name of fruit: ")
print("The English name of",a,"is",dict.get(a))