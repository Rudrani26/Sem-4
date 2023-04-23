class Inventory:
    def __init__(self):
        self.inventory = {}

    def addItems(self, id, name, stockCount, price):
        self.inventory[id] = {'name': name,
                              'stockCount': stockCount, 'price': price}

    def updateItem(self, id, stockCount, price):
        if id in self.inventory:
            self.inventory[id]['stockCount'] = stockCount
            self.inventory[id]['price'] = price
        else:
            print("Item not in inventory")

    def checkItemDetails(self, id):
        if id in self.inventory:
            item = self.inventory[id]
            return f"Product Name : {item['name']}, Stock Count : {item['stockCount']}, Price : {item['price']}"
        else:
            print("Item not in inventory")


inv = Inventory()

inv.addItems(1, "Hersheys", 250, 500)
inv.addItems(2, "Lindoor", 450, 900)
inv.addItems(3, "KitKat", 150, 300)
inv.addItems(4, "Kisses", 50, 100)

inv.updateItem(1, 125, 250)
inv.updateItem(3, 325, 650)

print(inv.checkItemDetails(1))
print(inv.checkItemDetails(2))
print(inv.checkItemDetails(3))
print(inv.checkItemDetails(4))
