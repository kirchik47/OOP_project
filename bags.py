import inspect
from collections import Counter


class BagsStore:
    def __init__(self, name):
        self.name = name
        self.stock = []
        self.profit = 0
        self.bags_counter = Counter()

    def add_to_stock(self, bag_inst):
        self.bags_counter[bag_inst] += 1
        print(self.bags_counter)
        if self.bags_counter[bag_inst] == 1:
            self.stock.append(bag_inst)
        self.profit -= bag_inst.price
        bag_inst.in_stock = True

    def sell(self, bag_inst):
        self.stock.pop(bag_inst)
        self.profit += bag_inst.price

    def get_current_stock(self):
        print("Current list of bags presented in the store:")
        for bag in self.stock:
            bag.get_description()
            print('number of bags:', self.bags_counter[bag])
            print('--------------------------------------')
            
        print(f"Current size of stock: {len(self.stock)}")

class Bag:
    def __init__(self, sex: str, material: str, brand: str, type: str, color: str, price: int, size: float):
        try:
            self.sex = sex
            self.material = material
            self.brand = brand
            self.type = type
            self.color = color
            self.price = price
            self.size = size
            self.in_stock = False
        except:
            print("Please enter the attributes based on instructions.")
    
    def get_description(self):
        for attribute in dir(self):
            if '__' not in attribute and not inspect.ismethod(getattr(self, attribute)):
                print(f'{attribute}: {getattr(self, attribute)}') 
    
bag = Bag('M', 'cotton', 'gucci', 'handbag', 'red', 1000, 30.5)
store = BagsStore('VOVA GANDON')
store.add_to_stock(bag)
store.add_to_stock(bag)
store.get_current_stock()
    