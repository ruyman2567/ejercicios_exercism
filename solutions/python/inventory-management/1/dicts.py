"""Functions to keep track and alter inventory."""


def create_inventory(items):
    dic={}
    for i in items:
        dic.setdefault(i,0)
        dic[i]+=1
    return dic


def add_items(inventory, items):
    for i in items:
        inventory.setdefault(i,0)
        inventory[i]+=1
    return inventory


def decrement_items(inventory, items):
    for i in items:
        if i in inventory:
            inventory[i]-=1
            if inventory[i]<0:
                inventory[i]=0
    return inventory


def remove_item(inventory, item):
    if item in inventory:
        inventory.pop(item)
        return inventory
    else:
        return inventory


def list_inventory(inventory):
    lista=[]
    for name,value in inventory.items():
        if (name in inventory) and (value>0):
            lista.append((name,value))
    return lista

