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
        if self.bags_counter[bag_inst] > 0:
            self.bags_counter[bag_inst] -= 1
            if self.bags_counter[bag_inst] == 0:
                self.stock.remove(bag_inst)
            self.profit += bag_inst.price
            return True
        else:
            return False
        
    def get_current_stock(self):
        print("Current list of bags presented in the store:")
        for i, bag in enumerate(self.stock):
            print('index:', i + 1)
            print(bag.get_description())
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
    def __init__(self, material: str, brand: str, color: str, price: float, size: float, num_of_compartments: int, has_side_pockets: bool,
                 has_hip_belt: bool, has_usb_port: bool, has_laptop_sleeve: bool):
        super().__init__(material, brand, color, price, size)
        self.num_of_compartments = num_of_compartments
        self.has_side_pockets = has_side_pockets
        self.has_hip_belt = has_hip_belt
        self.has_usb_port = has_usb_port
        self.has_laptop_sleeve = has_laptop_sleeve

    def get_description(self):
        desc = f"A {self.size} {self.color}, {self.brand} backpack made of {self.material}, with {self.num_of_compartments} compartments, "
        desc += "with side pockets for a bottle, " if self.has_side_pockets else "without side pockets for a bottle, "
        desc += "with hip belt, " if self.has_side_pockets else "without hip belt, "
        desc += "with usb port, " if self.has_side_pockets else "without usb port, "
        desc += "with laptop sleeve." if self.has_side_pockets else "without laptop sleeve."
        return desc + f"\nThe price is {self.price}."


class Handbag(Bag):
    def __init__(self, material: str, brand: str, color: str, price: int, size: float, has_long_strap: bool):
        super().__init__(material, brand, color, price, size)
        self.has_long_strap = has_long_strap
    
    def get_description(self):
        desc = f"A {self.size} {self.color}, {self.brand} handbag made of {self.material}, "
        desc += "with long strap." if self.has_long_strap else "without long strap."
        return desc + f"\nThe price is {self.price}."

class DuffelBag(Bag):
    def __init__(self, material: str, brand: str, color: str, price: int, size: float, is_waterproof: bool, has_shoe_compartment: bool):
        super().__init__(material, brand, color, price, size)
        self.is_waterproof = is_waterproof
        self.has_shoe_compartment = has_shoe_compartment
    
    def get_description(self):
        desc = f"A {self.size} {self.color}, {self.brand} duffel bag made of {self.material}, "
        desc += "is waterproof, " if self.is_waterproof else "is not waterproof, "
        desc += "with shoe compartment." if self.has_shoe_compartment else "without shoe compartment."
        return desc + f"\nThe price is {self.price}."
    

class MessengerBag(Bag):
    def __init__(self, material: str, brand: str, color: str, price: int, size: float, has_laptop_sleeve: bool, has_padded_strap: bool):
        super().__init__(material, brand, color, price, size)
        self.has_laptop_sleeve = has_laptop_sleeve
        self.has_padded_strap = has_padded_strap
    
    def get_description(self):
        desc = f"A {self.size} {self.color}, {self.brand} messenger bag made of {self.material}, "
        desc += "with laptop sleeve, " if self.has_laptop_sleeve else "without laptop sleeve, "
        desc += "with padded_strap." if self.has_padded_strap else "without padded_strap."
        return desc + f"\nThe price is {self.price}."
    

class ToteBag(Bag):
    def __init__(self, material: str, brand: str, color: str, price: int, size: float, has_zipper: bool):
        super().__init__(material, brand, color, price, size)
        self.has_zipper = has_zipper
    
    def get_description(self):
        desc = f"A {self.size} {self.color}, {self.brand} tote bag made of {self.material}, "
        desc += "with zipper." if self.has_zipper else "without zipper."
        return desc + f"\nThe price is {self.price}."
    

if __name__ == '__main__':
    store = BagsStore('dsf')
    backpack = Backpack('cotton', 'nike', 'red', 1000.0, 10.5, 5, True, True, True, True)
    store.add_to_stock(backpack)
    store.get_current_stock()
