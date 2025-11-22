inventory = () #создаем кортеж

#рассмотрим его как условие кориежа (интвентаря)
if not inventory:
    print("Inventory is empty") # проверка есть ли что то в инвентаре, инвентарь пуст
input("enter to exit")

inventory = ("sword",
             "shield",
             "chain",
             "heal potion") #заполним инвентарь новым кортежом
print("\nShow inventory")
print(inventory)

for item in inventory:
    print(item)

input("enter to exit")

# страница 124 учебника