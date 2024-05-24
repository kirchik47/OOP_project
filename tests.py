import unittest
from bags import Backpack, Handbag, DuffelBag, MessengerBag, ToteBag


class TestBackpack(unittest.TestCase):
    def test_backpack_initialization(self):
        backpack = Backpack("nylon", "Nike", "blue", 100.0, 30.0, 5, True, True, True, True)
        self.assertEqual(backpack.material, "nylon")
        self.assertEqual(backpack.brand, "Nike")
        self.assertEqual(backpack.color, "blue")
        self.assertEqual(backpack.price, 100.0)
        self.assertEqual(backpack.size, 30.0)
        self.assertEqual(backpack.num_of_compartments, 5)
        self.assertTrue(backpack.side_pockets)
        self.assertTrue(backpack.hip_belt)
        self.assertTrue(backpack.usb_port)
        self.assertTrue(backpack.laptop_sleeve)

    def test_backpack_methods(self):
        backpack = Backpack("nylon", "Nike", "blue", 100.0, 30.0, 5, True, True, True, True)
        expected_description = ("A 30.0 blue, Nike backpack made of nylon, with 5 compartments, "
                                "with side pockets for a bottle, with hip belt, with usb port, with laptop sleeve.\n"
                                "The price is 100.0.")
        self.assertEqual(backpack.get_description(), expected_description)

class TestHandbag(unittest.TestCase):
    def test_handbag_initialization(self):
        handbag = Handbag("leather", "Gucci", "black", 200.0, 20.0, True)
        self.assertEqual(handbag.material, "leather")
        self.assertEqual(handbag.brand, "Gucci")
        self.assertEqual(handbag.color, "black")
        self.assertEqual(handbag.price, 200.0)
        self.assertEqual(handbag.size, 20.0)
        self.assertTrue(handbag.long_strap)

    def test_handbag_methods(self):
        handbag = Handbag("leather", "Gucci", "black", 200.0, 20.0, True)
        expected_description = ("A 20.0 black, Gucci handbag made of leather, with long strap.\n"
                                "The price is 200.0.")
        self.assertEqual(handbag.get_description(), expected_description)

class TestDuffelBag(unittest.TestCase):
    def test_duffel_bag_initialization(self):
        duffel_bag = DuffelBag("canvas", "Adidas", "red", 150.0, 40.0, True, True)
        self.assertEqual(duffel_bag.material, "canvas")
        self.assertEqual(duffel_bag.brand, "Adidas")
        self.assertEqual(duffel_bag.color, "red")
        self.assertEqual(duffel_bag.price, 150.0)
        self.assertEqual(duffel_bag.size, 40.0)
        self.assertTrue(duffel_bag.waterproof)
        self.assertTrue(duffel_bag.shoe_compartment)

    def test_duffel_bag_methods(self):
        duffel_bag = DuffelBag("canvas", "Adidas", "red", 150.0, 40.0, True, True)
        expected_description = ("A 40.0 red, Adidas duffel bag made of canvas, is waterproof, with shoe compartment.\n"
                                "The price is 150.0.")
        self.assertEqual(duffel_bag.get_description(), expected_description)

class TestMessengerBag(unittest.TestCase):
    def test_messenger_bag_initialization(self):
        messenger_bag = MessengerBag("fabric", "Puma", "grey", 120.0, 25.0, True, True)
        self.assertEqual(messenger_bag.material, "fabric")
        self.assertEqual(messenger_bag.brand, "Puma")
        self.assertEqual(messenger_bag.color, "grey")
        self.assertEqual(messenger_bag.price, 120.0)
        self.assertEqual(messenger_bag.size, 25.0)
        self.assertTrue(messenger_bag.laptop_sleeve)
        self.assertTrue(messenger_bag.padded_strap)

    def test_messenger_bag_methods(self):
        messenger_bag = MessengerBag("fabric", "Puma", "grey", 120.0, 25.0, True, True)
        expected_description = ("A 25.0 grey, Puma messenger bag made of fabric, with laptop sleeve, with padded_strap.\n"
                                "The price is 120.0.")
        self.assertEqual(messenger_bag.get_description(), expected_description)

class TestToteBag(unittest.TestCase):
    def test_tote_bag_initialization(self):
        tote_bag = ToteBag("cotton", "Levi's", "white", 80.0, 35.0, True)
        self.assertEqual(tote_bag.material, "cotton")
        self.assertEqual(tote_bag.brand, "Levi's")
        self.assertEqual(tote_bag.color, "white")
        self.assertEqual(tote_bag.price, 80.0)
        self.assertEqual(tote_bag.size, 35.0)
        self.assertTrue(tote_bag.zipper)

    def test_tote_bag_methods(self):
        tote_bag = ToteBag("cotton", "Levi's", "white", 80.0, 35.0, True)
        expected_description = ("A 35.0 white, Levi's tote bag made of cotton, with zipper.\n"
                                "The price is 80.0.")
        self.assertEqual(tote_bag.get_description(), expected_description)

if __name__ == '__main__':
    unittest.main()