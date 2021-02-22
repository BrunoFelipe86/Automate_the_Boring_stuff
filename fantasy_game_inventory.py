def displayInventory (inventory):
    print ("Inventory:")
    item_total = 0
    for keys, valoues in inventory.items():
        print (str(valoues) + ":" + keys)
        a = valoues
        item_total = item_total + a


    print ("Total number of item:" + str(item_total))



stuff = {'espadas':12,'corda':34,'escudos':33,'adagas':123,'moedas':12}

displayInventory(stuff)