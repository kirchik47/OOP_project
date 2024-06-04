import unittest
from bags import Bag, Mannequin, Backpack, Handbag, ToteBag, MessengerBag, DuffelBag


class Mannequin:
    def __init__(self):
        self.is_carrying_bag = False
    
    def take_off_bag(self):
        if self.is_carrying_bag:
            self.is_carrying_bag = False
            return "The bag is taken off."
        return "No bag is carried."

class Bag:
    def __init__(self, material: str, brand: str, color: str, price: float, size: float):
        self.material = material
        self.brand = brand
        self.color = color
        self.price = price
        self.size = size

class TestMannequin(unittest.TestCase):
    def test_mannequin_initialization(self):
        mannequin = Mannequin()
        self.assertFalse(mannequin.is_carrying_bag)

    def test_take_off_bag(self):
        mannequin = Mannequin()
        self.assertEqual(mannequin.take_off_bag(), "No bag is carried.")
        mannequin.is_carrying_bag = True
        self.assertEqual(mannequin.take_off_bag(), "The bag is taken off.")
        self.assertFalse(mannequin.is_carrying_bag)

class TestBackpack(unittest.TestCase):
    def test_backpack_initialization(self):
        backpack = Backpack("nylon", "Nike", "blue", 100.0, 30.0, 5, True, True, True, True)
        self.assertEqual(backpack.material, "nylon")
        self.assertEqual(backpack.brand, "Nike")
        self.assertEqual(backpack.color, "blue")
        self.assertEqual(backpack.price, 100.0)
        self.assertEqual(backpack.size, 30.0)
        self.assertEqual(backpack.num_of_compartments, 5)
        self.assertTrue(backpack.has_side_pockets)
        self.assertTrue(backpack.has_hip_belt)
        self.assertTrue(backpack.has_usb_port)
        self.assertTrue(backpack.has_laptop_sleeve)

    def test_backpack_methods(self):
        backpack = Backpack("nylon", "Nike", "blue", 100.0, 30.0, 5, True, True, True, True)
        expected_description = ("A 30.0 blue, Nike backpack made of nylon, with 5 compartments, "
                                "with side pockets for a bottle, with hip belt, with usb port, with laptop sleeve.\n"
                                "The price is 100.0.")
        self.assertEqual(backpack.get_description(), expected_description)
        mannequin = Mannequin()
        self.assertEqual(backpack.carry(mannequin), "Mannequin is carrying a backpack on the back using both shoulder straps.")
        self.assertTrue(mannequin.is_carrying_bag)
        self.assertEqual(backpack.carry(mannequin), "Mannequin is already carrying a bag.")
        self.assertEqual(backpack.packing_instructions(), "Pack heavier items at the bottom and lighter items at the top. Utilize side pockets for quick access items.")
        self.assertEqual(backpack.display_use_case(), "Ideal for students and hikers who need to carry multiple items.")
        mannequin.take_off_bag()

class TestHandbag(unittest.TestCase):
    def test_handbag_initialization(self):
        handbag = Handbag("leather", "Gucci", "black", 200.0, 20.0, True)
        self.assertEqual(handbag.material, "leather")
        self.assertEqual(handbag.brand, "Gucci")
        self.assertEqual(handbag.color, "black")
        self.assertEqual(handbag.price, 200.0)
        self.assertEqual(handbag.size, 20.0)
        self.assertTrue(handbag.has_long_strap)

    def test_handbag_methods(self):
        handbag = Handbag("leather", "Gucci", "black", 200.0, 20.0, True)
        expected_description = ("A 20.0 black, Gucci handbag made of leather, with long strap.\n"
                                "The price is 200.0.")
        self.assertEqual(handbag.get_description(), expected_description)
        mannequin = Mannequin()
        self.assertEqual(handbag.carry(mannequin), "Mannequin is carrying a handbag over the shoulder using the strap.")
        self.assertTrue(mannequin.is_carrying_bag)
        self.assertEqual(handbag.carry(mannequin), "Mannequin is already carrying a bag.")
        self.assertEqual(handbag.packing_instructions(), "Organize items with the most frequently used ones on top. Secure valuables in internal pockets.")
        self.assertEqual(handbag.display_use_case(), "Perfect for daily use and casual outings.")
        mannequin.take_off_bag()

class TestDuffelBag(unittest.TestCase):
    def test_duffel_bag_initialization(self):
        duffel_bag = DuffelBag("canvas", "Adidas", "red", 150.0, 40.0, True, True)
        self.assertEqual(duffel_bag.material, "canvas")
        self.assertEqual(duffel_bag.brand, "Adidas")
        self.assertEqual(duffel_bag.color, "red")
        self.assertEqual(duffel_bag.price, 150.0)
        self.assertEqual(duffel_bag.size, 40.0)
        self.assertTrue(duffel_bag.is_waterproof)
        self.assertTrue(duffel_bag.has_shoe_compartment)

    def test_duffel_bag_methods(self):
        duffel_bag = DuffelBag("canvas", "Adidas", "red", 150.0, 40.0, True, True)
        expected_description = ("A 40.0 red, Adidas duffel bag made of canvas, is waterproof, with shoe compartment.\n"
                                "The price is 150.0.")
        self.assertEqual(duffel_bag.get_description(), expected_description)
        mannequin = Mannequin()
        self.assertEqual(duffel_bag.carry(mannequin), "Mannequin is carrying a duffel bag by hand using the handles.")
        self.assertTrue(mannequin.is_carrying_bag)
        self.assertEqual(duffel_bag.carry(mannequin), "Mannequin is already carrying a bag.")
        self.assertEqual(duffel_bag.packing_instructions(), "Use shoe compartment for shoes or dirty laundry. Pack clothes in the main compartment.")
        self.assertEqual(duffel_bag.display_use_case(), "Great for gym sessions and weekend trips.")
        mannequin.take_off_bag()

class TestMessengerBag(unittest.TestCase):
    def test_messenger_bag_initialization(self):
        messenger_bag = MessengerBag("fabric", "Puma", "grey", 120.0, 25.0, True, True)
        self.assertEqual(messenger_bag.material, "fabric")
        self.assertEqual(messenger_bag.brand, "Puma")
        self.assertEqual(messenger_bag.color, "grey")
        self.assertEqual(messenger_bag.price, 120.0)
        self.assertEqual(messenger_bag.size, 25.0)
        self.assertTrue(messenger_bag.has_laptop_sleeve)
        self.assertTrue(messenger_bag.has_padded_strap)

    def test_messenger_bag_methods(self):
        messenger_bag = MessengerBag("fabric", "Puma", "grey", 120.0, 25.0, True, True)
        expected_description = ("A 25.0 grey, Puma messenger bag made of fabric, with laptop sleeve, with padded strap.\n"
                                "The price is 120.0.")
        self.assertEqual(messenger_bag.get_description(), expected_description)
        mannequin = Mannequin()
        self.assertEqual(messenger_bag.carry(mannequin), "Mannequin is carrying a messenger bag over shoulder")
        self.assertTrue(mannequin.is_carrying_bag)
        self.assertEqual(messenger_bag.carry(mannequin), "Mannequin is already carrying a bag.")
        self.assertEqual(messenger_bag.packing_instructions(), "Place the laptop in the designated sleeve and use other compartments for documents and small gadgets.")
        self.assertEqual(messenger_bag.display_use_case(), "Suitable for professionals and students who need to carry a laptop and documents.")
        mannequin.take_off_bag()

class TestToteBag(unittest.TestCase):
    def test_tote_bag_initialization(self):
        tote_bag = ToteBag("cotton", "Levi's", "white", 80.0, 35.0, True)
        self.assertEqual(tote_bag.material, "cotton")
        self.assertEqual(tote_bag.brand, "Levi's")
        self.assertEqual(tote_bag.color, "white")
        self.assertEqual(tote_bag.price, 80.0)
        self.assertEqual(tote_bag.size, 35.0)
        self.assertTrue(tote_bag.has_zipper)

    def test_tote_bag_methods(self):
        tote_bag = ToteBag("cotton", "Levi's", "white", 80.0, 35.0, True)
        expected_description = ("A 35.0 white, Levi's tote bag made of cotton, with zipper.\n"
                                "The price is 80.0.")
        self.assertEqual(tote_bag.get_description(), expected_description)
        mannequin = Mannequin()
        self.assertEqual(tote_bag.carry(mannequin), "Mannequin is carrying a tote bag by hand")
        self.assertTrue(mannequin.is_carrying_bag)
        self.assertEqual(tote_bag.carry(mannequin), "Mannequin is already carrying a bag.")
        self.assertEqual(tote_bag.packing_instructions(), "Use the main compartment for larger items and small pockets for keys and phone.")
        self.assertEqual(tote_bag.display_use_case(), "Ideal for shopping and casual outings.")
        mannequin.take_off_bag()

if __name__ == '__main__':
    unittest.main()
