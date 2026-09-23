# Oefening 1
# Print de volgende zin "Hello World"

print("Hello World")


# Oefening 2
# Verander de waarde van de onderstaande variabelen.
# Print deze daarna 1 voor 1 uit

naam = "Dawit"
leeftijd = 23
woonstad = "Utrecht"


# Oefening 3
# Gebruik nu bovenstaande variabelen om zinnen te bouwen
# Bijvoorbeeld print("Hallo mijn naam is ", naam) of print(f"Mijn naam is {naam}")

print("Hallo mijn naam is", naam)
print(f"Mijn naam is {naam}")
print(f"Ik ben {leeftijd} jaar oud en woon in {woonstad}")


# Oefening 4
# Maak variabelen aan voor je favoriete game, hoe veel uur je deze hebt gespeeld en welk cijfer je dit spel zou geven
# Print deze daarna in zinnen uit, bijvoorbeeld "Mijn favoriete game is Minecraft" "Ik heb deze game 150 uur gespeeld", "Ik geef deze game een 8.5"

favoriete_game = "GTA V"
uren_gespeeld = 200
cijfer = 9

print(f"Mijn favoriete game is {favoriete_game}, ik heb hem {uren_gespeeld} uur gespeeld en geef het spel een {cijfer}.")

# Oefening 5
# Maak twee variabelen aan, number1 en number2
# Bereken daarna de som (+), het verschil (-) en het product (*) uit van deze nummers.
# Print daarna de uitkomsten uit

number1 = 10
number2 = 5

som = number1 + number2
verschil = number1 - number2
product = number1 * number2

print("Som:", som)
print("Verschil:", verschil)
print("Product:", product)

# Oefening 6
# Maak een simpel game character met minimaal de volgende variabelen: name, health, level, damage
# Print deze vervolgens uit
# Zorg er daarna voor dat je character 20 damage neemt, print nu de nieuwe waarde van zijn health uit

name = "Warrior"
health = 100
level = 5
damage = 20

print("Naam:", name)
print("Health:", health)
print("Level:", level)
print("Damage:", damage)

health = health - 20

print("Nieuwe health:", health)

# Oefening 7
# Ga verder met je character van de vorige oefening. Voeg nu een nieuw variabel "weapon" toe.
# Geef het wapen een naam, verhoog de damage van je character en verhoog het level met 1
# Print daarna de nieuwe waardes uit 

# Oefening 7

weapon = "Sword"
damage = damage + 10
level = level + 1

print("Naam:", name)
print("Health:", health)
print("Level:", level)
print("Damage:", damage)
print("Weapon:", weapon)

# Oefening 8
# Maak een programma dat een profiel van een gamer laat zien
# Maak minimaal de volgende variabelen: name, age, favouriteGame, hoursPlayed, level, score
# Print al deze informatie netjes uit
# Verhoog daarna de score van het profiel met 250 en print de nieuwe waarde
# Bonus! Voeg zelf 3 nieuwe variabelen toe

# Oefening 8

name = "Dawit"
age = 23
favouriteGame = "GTA V"
hoursPlayed = 200
level = 10
score = 1000

print("Naam:", name)
print("Leeftijd:", age)
print("Favoriete game:", favouriteGame)
print("Uren gespeeld:", hoursPlayed)
print("Level:", level)
print("Score:", score)

score = score + 250

print("Nieuwe score:", score)