name = 'Nguyen Quoc An'  # (1) REPLACE THE STRING VARIABLE WITH YOUR NAME in string type
student_num = '7769428' # (2) REPLACE THIS STRING VARIABLE WITH YOUR UOW ID in string type
subject_code = 'CSIT110'

import re

# (2) insert class and function definitions here.

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

    oosCount = 0
    validCount = 0

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
                cls.oosCount+=1
                raise OutOfStockError(item)
            if qty > 0:
                cls.validCount+=1
                Y[item] = qty
        return Y    

#3b
def collate_orders(N):
    invalidCount = 0
    
    for i in range(0,N):
        try:
            Inventory.order()
        except OutOfStockError:
            pass
        except:
            invalidCount+=1
            #print("Invalid input format")

    Z = {'invalid':invalidCount,'valid':Inventory.validCount,'oos':Inventory.oosCount}
    return Z

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
    remainderLetters = ['A','Z','Y','X','U','T','S','R','P','M','L','K','J','H','G','E','D','C','B']
    
    prefix = re.findall("\D", i)
    if len(prefix)>2:
        prefix = [letters.index(prefix[1])+1, letters.index(prefix[2])+1]
    elif len(prefix)<2:
        prefix = [0, letters.index(prefix[0])+1]
    
    numbers = re.findall("\d",i)
    numberList = []
    for i in range(0,len(numbers)):
        numberList.append(int(numbers[i]))
        
    missing = 4 - len(numberList)
    for i in range(0,missing):
        numberList.insert(0,0)
        
    final = (prefix[0]*9 +prefix[1]*4 +numberList[0]*5 +numberList[1]*4 +numberList[2]*3 +numberList[3]*2)%19
    
    return remainderLetters[final]
 
def main():
    print("Assignment 3")
    #Question 1
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

    #Question 3
    #3a
    Inventory.set_items_from_list([["Eggs", 2.98, 12],["Milk", 4.65, 8],["Tea", 1.50, 6]])
    print(Inventory.items)
    print(Inventory.order())
    Inventory.order()

    #3b
    Inventory.set_items_from_list([["Eggs", 2.98, 12],["Milk", 4.65, 8],["Tea", 1.50, 6]])
    print(Inventory.items)
    print(collate_orders(4))

    #Question 4
    #4a
    get_nric_checksum(1234567)

    #4b
    get_vehicle_plate_checksum("SBS3229")
    
if __name__ == "__main__":
    main()