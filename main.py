#List:
#lista = [1,2,3]
#Tienen un orden
#Empieza en 0


states_of_the_US = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]

print(states_of_the_US[0])

#Si lo combinamos con un String
print(f"The first state that joined the US was {states_of_the_US[0]}")

#Cuenta desde the end of the list
print(states_of_the_US[-1])

dirty_dozen = ["Strawberries", "Spinach", "Kale", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears", "Tomatoes", "Celery", "Potatoes"]

#Change un elemento de la list
dirty_dozen[1] = "Espinacas"

print(dirty_dozen)

#Add to the list at the end
dirty_dozen.append("Papas")

print(dirty_dozen)

#Add a list to the list

dirty_dozen.extend(["Zapallo", "Zanahoria", "Batata"])

print(dirty_dozen)