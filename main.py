inventory = () #создаем кортеж

#рассмотрим его как условие кориежа (интвентаря)
if not inventory:
    print("\tInventory is empty") # проверка есть ли что то в инвентаре, инвентарь пуст
input("Press to continue")

inventory = ("sword",
             "shield",
             "chain",
             "heal potion") #заполним инвентарь новым кортежом
print("\nShow inventory")
print(inventory)

for item in inventory:
    print("\t" + item)

input("Press to continue")

ans = input("You found chest. Would you like to open? y|n")
if ans == "y":
    chest = ("Mana Potion", "Helmet")
    for item in chest:
        print("\t" + item)
    ans = input("Take or not? y|n")
    if ans == "y":
        inventory += chest
        print("\tInventory: ")
        for item in inventory:
            print("\t" + item)
    else:
        print("\tInventory: ")
        for item in inventory:
            print("\t" + item)
else:
    print("You did not take anything")
# страница 136 учебника