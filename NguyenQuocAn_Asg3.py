import re

#Question 1
class Price:
#1a
    currency = "SGD"
    def __init__(self, value):
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
            cls.items[aList[i][0]] = {"price": '$'+str(aList[i][1]), "stock": aList[i][2]}
    
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
    invalidCount = 0
    oosCount = 0
    validCount = 0
    for i in range(0,N):
        try:
            Inventory.order()
        except OutOfStockError:
            oosCount+=1
        except:
            invalidCount+=1
        else:
            validCount+=1          
    print(f"'invalid': {invalidCount}, 'valid':{validCount}, 'oos': {oosCount}")


#Question 4
#4a
def get_nric_checksum(i):
    i = str(i)
    d = (2*int(i[0]) + 7*int(i[1]) + 6*int(i[2]) + 5*int(i[3]) + 4*int(i[4]) + 3*int(i[5]) + 2*int(i[6])) % 11
    if d == 10: return 'A'
    elif d == 9: return 'B'
    elif d == 8: return 'C'
    elif d == 7: return 'D'
    elif d == 6: return 'E'
    elif d == 5: return 'F'
    elif d == 4: return 'G'
    elif d == 3: return 'H'
    elif d == 2: return 'I'
    elif d == 1: return 'Z'
    elif d == 0: return 'J'

#4b
def get_vehicle_plate_checksum(i):
    letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    i="S3229"
    prefix = re.findall("\D", i)
    if len(prefix)>2:
        prefix = prefix[1:3]
    elif len(prefix)<2:
        prefix = [0, prefix[0]]
    
    prefix
get_vehicle_plate_checksum("SBS3229") 



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
print(Inventory.items["Eggs"]["price"])
#3a
Inventory.set_items_from_list([["Eggs", 2.98, 12],["Milk", 4.65, 8],["Tea", 1.50, 6]])
print(Inventory.items)
print(Inventory.order())
Inventory.order()

#3b
Inventory.set_items_from_list([["Eggs", 2.98, 12],["Milk", 4.65, 8],["Tea", 1.50, 6]])

print(collate_orders(4))

