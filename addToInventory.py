def addToInventory (inventory, additem):
    for item in additem:
        inventory.setdefault(item,0)
        inventory[item] +=1
    return inventory


def displayInventory (inventory):
    print ("Inventory:")
    item_total = 0
    for keys, valoues in inventory.items():
        print (str(valoues) + ":" + keys)
        a = valoues
        item_total = item_total + a

    print ("Total number of item:" + str(item_total))


inv = {'gold coin': 40 , 'rope': 1 }
displayInventory(inv)
tesouro  = ['gold coin', 'adaga', 'gold coin', 'ruby']
addToInventory(inv, tesouro)
displayInventory(inv)


