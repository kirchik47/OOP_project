import inspect
from collections import Counter
import time
import json
import unittest


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
        bag_inst.__time_added_to_stock = time.time()
    def sell(self, bag_inst):
        self.stock.pop(bag_inst)
        self.profit += bag_inst.price

    def get_current_stock(self):
        print("Current list of bags presented in the store:")
        for i, bag in enumerate(self.stock):
            print('index:', i + 1)
            bag.get_description()
            print('number of bags:', self.bags_counter[bag])
            print('--------------------------------------')
            
        print(f"Current size of stock: {len(self.stock)}")

class Bag:
    def __init__(self, material: str, brand: str, color: str, price: int, size: float):
        self.material = material
        self.brand = brand
        self.color = color
        self.price = price
        self.size = size
    

class Backpack(Bag):
    def __init__(self, material: str, brand: str, color: str, price: float, size: float, num_of_compartments: int, side_pockets: bool,
                 hip_belt: bool, usb_port: bool, laptop_sleeve: bool):
        super().__init__(material, brand, color, price, size)
        self.num_of_compartments = num_of_compartments
        self.side_pockets = side_pockets
        self.hip_belt = hip_belt
        self.usb_port = usb_port
        self.laptop_sleeve = laptop_sleeve

    def get_description(self):
        desc = f"A {self.size} {self.color}, {self.brand} backpack made of {self.material}, with {self.num_of_compartments} compartments, "
        desc += "with side pockets for a bottle, " if self.side_pockets else "without side pockets for a bottle, "
        desc += "with hip belt, " if self.side_pockets else "without hip belt, "
        desc += "with usb port, " if self.side_pockets else "without usb port, "
        desc += "with laptop sleeve." if self.side_pockets else "without laptop sleeve."
        return desc + f"\nThe price is {self.price}."


class Handbag(Bag):
    def __init__(self, material: str, brand: str, color: str, price: int, size: float, long_strap: bool):
        super().__init__(material, brand, color, price, size)
        self.long_strap = long_strap
    
    def get_description(self):
        desc = f"A {self.size} {self.color}, {self.brand} handbag made of {self.material}, "
        desc += "with long strap." if self.long_strap else "without long strap."
        return desc + f"\nThe price is {self.price}."

class DuffelBag(Bag):
    def __init__(self, material: str, brand: str, color: str, price: int, size: float, waterproof: bool, shoe_compartment: bool):
        super().__init__(material, brand, color, price, size)
        self.waterproof = waterproof
        self.shoe_compartment = shoe_compartment
    
    def get_description(self):
        desc = f"A {self.size} {self.color}, {self.brand} duffel bag made of {self.material}, "
        desc += "is waterproof, " if self.waterproof else "is not waterproof, "
        desc += "with shoe compartment." if self.shoe_compartment else "without shoe compartment."
        return desc + f"\nThe price is {self.price}."
    

class MessengerBag(Bag):
    def __init__(self, material: str, brand: str, color: str, price: int, size: float, laptop_sleeve: bool, padded_strap: bool):
        super().__init__(material, brand, color, price, size)
        self.laptop_sleeve = laptop_sleeve
        self.padded_strap = padded_strap
    
    def get_description(self):
        desc = f"A {self.size} {self.color}, {self.brand} messenger bag made of {self.material}, "
        desc += "with laptop sleeve, " if self.laptop_sleeve else "without laptop sleeve, "
        desc += "with padded_strap." if self.padded_strap else "without padded_strap."
        return desc + f"\nThe price is {self.price}."
    

class ToteBag(Bag):
    def __init__(self, material: str, brand: str, color: str, price: int, size: float, zipper: bool):
        super().__init__(material, brand, color, price, size)
        self.zipper = zipper
    
    def get_description(self):
        desc = f"A {self.size} {self.color}, {self.brand} tote bag made of {self.material}, "
        desc += "with zipper." if self.zipper else "without zipper."
        return desc + f"\nThe price is {self.price}."
    

if __name__ == '__main__':
    bag = Backpack('cotton', 'gucci', 'red', 1000, 30.5, 5, True, True, True, True)
    print(bag.get_description())
    store = BagsStore('VOVA GANDON')
    store.add_to_stock(bag)
    store.add_to_stock(bag)
    store.get_current_stock()
    