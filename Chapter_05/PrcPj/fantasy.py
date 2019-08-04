'''
Fantasy Game Inventory
You are creating a fantasy video game. The data structure to model the
player’s inventory will be a dictionary where the keys are string values
describing the item in the inventory and the value is an integer value detail-
ing how many of that item the player has. For example, the dictionary value
{'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12} means the
player has 1 rope, 6 torches, 42 gold coins, and so on.
    Write a function named displayInventory() that would take any possible
“inventory” and display it like the following:

--------------------------------------------------------------------------------
Inventory:
12 arrow
42 gold coin
1 rope
6 torch
1 dagger
Total number of items: 62
--------------------------------------------------------------------------------

Hint: You can use a for loop to loop through all the keys in a dictionary.

--------------------------------------------------------------------------------
# inventory.py
stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        print(str(v) + ' ' + k)
        item_total += v
    print("Total number of items: " + str(item_total))
displayInventory(stuff)

--------------------------------------------------------------------------------
'''

itemList = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}     

while True:
    print('Enter an item(s). Type empty value to use default list: ')
    itemName = input()
    if itemName == '':
        break

    if itemName in itemList:
        print('This item is already in your inventory.')
    else:
        print('Add new item quantity...')
        newItemQty = input()
        itemList[itemName] = int(newItemQty)
        print('Inventory updated.')

print('Waiting for processing ....')

def displayInventory(inventoryList):
    print('Inventory: ')
    total_items = 0
    # During for i, j somelist.items() -> i = keyName , j = keyValue
    for i, j in inventoryList.items():
        print(str(j) + '\t\t' + i)
        total_items += j
    print('Total number of items: ' + str(total_items))


displayInventory(itemList)

