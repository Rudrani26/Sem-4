class Restaurant:
    def __init__(self):
        self.menuItems = {}
        self.bookTable = []
        self.customerOrder = []

    def addItems_onMenu(self, item, price):
        self.menuItems[item] = price

    def tableReservations(self, tableNumber):
        self.bookTable.append(tableNumber)

    def takeOrder(self, tableNumber, item):
        orderDetails = {'tableNumber': tableNumber, 'item': item}
        self.customerOrder.append(orderDetails)

    def printMenu(self):
        for item, price in self.menuItems.items():
            print("{} : {}".format(item, price))

    def printReservation(self):
        for table in self.bookTable:
            print("Table : {}".format(table))

    def printOrders(self):
        for orderDetails in self.customerOrder:
            print("Table {} : {}".format(
                orderDetails['tableNumber'], orderDetails['item']))


restaurant = Restaurant()

restaurant.addItems_onMenu("Chicken Tikka", 350)
restaurant.addItems_onMenu("Tandoori Roti", 150)
restaurant.addItems_onMenu("Masala Papad", 50)
restaurant.addItems_onMenu("Prawns Koliwada", 450)

print("==============MENU ITEMS=============")
restaurant.printMenu()

restaurant.tableReservations(1)
restaurant.tableReservations(4)
restaurant.tableReservations(6)
restaurant.tableReservations(3)

print("==============TABLE RESERVATIONS=============")
restaurant.printReservation()

restaurant.takeOrder(1, "Chicken Tikka")
restaurant.takeOrder(1, "Tandoori Roti")
restaurant.takeOrder(4, "Masala Papad")
restaurant.takeOrder(3, "Prawns Koliwada")
restaurant.takeOrder(6, "Water")

print("==============ORDERS=============")
restaurant.printOrders()
