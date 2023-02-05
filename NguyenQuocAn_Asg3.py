#Question 1
class Price:
#1a
    currency = "SGD"
    def __init__(self, value) -> None:
        self.value = value 

#1b
    def __str__(self):
        return f"${self.value:.2f}"
    
    def __repr__(self):
        return f"${self.value:.2f}"

#1c
class OutOfStockError(Exception):
    def __init__(self, itemName):
        self.itemName = itemName
    
    def  __str__(self):
        return f"The following item {self.itemName} is out of stock"

#Question 2
#2a
class Inventory():
    hotline = "1800-1333-5432" 
    items = {}

#2b
    @classmethod
    def set_items_from_list(cls, aList):
        for i in range(0,len(aList)):
            cls.items[aList[i][0]] = {"price": aList[i][1], "stock": aList[i][2]}
    
#3a
    @classmethod
    def order(cls):
        Y = {}
        for item in cls.items:
            qty = int(input(f"How many {item} would you like to order?"))
            if qty>cls.items[item]["stock"]:
                raise OutOfStockError(item)
            if qty > 0:
                Y[item] = qty
        return Y    

#3b
def collate_orders(N):
    Z = {"invalid","valid","oos"}
    try:
        for i in range(0,N+1):
            Inventory.order()
    
#1a       
pricetag = Price(2.89)
print(pricetag)
print(repr(pricetag)) 

#1c
try:
    raise OutOfStockError("Eggs")
except OutOfStockError as e:
    print(e)
    
#Question 2
#2a
print(Inventory.hotline)
print(Inventory.items)

#2b
print(Inventory.items)
Inventory.set_items_from_list([["Eggs", 2.98, 12],["Milk", 4.65, 3]])
print(Inventory.items)

#3a
Inventory.set_items_from_list([["Eggs", 2.98, 12],["Milk", 4.65, 8],["Tea", 1.50, 6]])
print(Inventory.items)
print(Inventory.order())
Inventory.order()
