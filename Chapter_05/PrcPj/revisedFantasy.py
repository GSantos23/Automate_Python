'''
List to Dictionary Function for Fantasy Game Inventory
Imagine that a vanquished dragon’s loot is represented as a list of strings
like this:
-------------------------------------------------------------------------------
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
-------------------------------------------------------------------------------

    Write a function named addToInventory(inventory, addedItems) , where the
inventory parameter is a dictionary representing the player’s inventory (like
in the previous project) and the addedItems parameter is a list like dragonLoot.

The addToInventory() function should return a dictionary that represents the
updated inventory. Note that the addedItems list can contain multiples of the
same item. Your code could look something like this:

--------------------------------------------------------------------------------
def addToInventory(inventory, addedItems):
    # your code goes here

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)
--------------------------------------------------------------------------------

The previous program (with your displayInventory() function from the
previous project) would output the following:

--------------------------------------------------------------------------------
Inventory:
45 gold coin
1 rope
1 ruby
1 dagger
Total number of items: 48
--------------------------------------------------------------------------------
'''
def displayInventory(inventoryList):
    ''' Displays inventory items '''
    print('Inventory: ')
    total_items = 0
    # During for i, j somelist.items() -> i = keyName , j = keyValue
    for i, j in inventoryList.items():
        print(str(j) + '\t\t' + i)
        total_items += j
    print('Total number of items: ' + str(total_items))


def addToInventory(inventory, addedItems):
    ''' Returns a dictionary that represents updated inventory '''
    print('Processing ...')
    newDic = {}     # Empty dictionary

    for k,v in inventory.items():
        for i in addedItems:

            if i == k:      # If dict in list
                v += 1
                newDic[k] = v

            elif i not in inventory.keys(): # if not item in keys
                newDic[i] = addedItems.count(i)

            else:               # no match with list
                newDic[k] = v
            
    return newDic

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin',  'dagger', 'gold coin', 'gold coin', 'ruby']
inv2 = addToInventory(inv, dragonLoot)
displayInventory(inv2)