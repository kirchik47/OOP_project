from bags import BagsStore, Bag, Backpack, Handbag, DuffelBag, MessengerBag, ToteBag 
import inspect



def get_user_attrs(choice):
    class_choice = class_mapper[choice]
    # print(inspect.signature(class_choice.__init__).parameters)
    user_params = []
    for attr in inspect.signature(class_choice.__init__).parameters:
        if attr == 'self':
             continue
        attr = attr.replace('_', ' ')
        param = input(f"Please enter the {attr}:\n" if attr in ['material', 'size', 'brand', 'color', 'price', 'num of compartments'] 
                      else f"Please enter whether it {attr}\n1. Yes\n2. No\n")
        if attr in ['num of compartments']:
             param = int(param)
        elif attr in ['price', 'size']:
             param = float(param)
        elif attr not in ['color', 'brand', 'material']:
             param = bool(param)             
        user_params.append(param)
    return user_params

store = BagsStore('LVSHOP')
class_mapper = {'1': Backpack,
                    '2': Handbag,
                    '3': DuffelBag,
                    '4': MessengerBag,
                    '5': ToteBag}
while True:
        print("\nWelcome to the bag store!")
        print("1. Add a bag to stock")
        print("2. Buy a bag")
        print("3. View current stock")
        print("4. Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            print("\nChoose a bag type to add:")
            print("1. Backpack")
            print("2. Handbag")
            print("3. Duffel Bag")
            print("4. Messenger Bag")
            print("5. Tote Bag")
            bag_choice = input("Enter your choice: ")
            bag = class_mapper[bag_choice](*get_user_attrs(bag_choice))
            store.add_to_stock(bag)
            print("Thank you for selling this bag!")
            
        
        elif choice == '2':
            print("\nChoose a bag type to buy:")
            print("1. Backpack")
            print("2. Handbag")
            print("3. Duffel Bag")
            print("4. Messenger Bag")
            print("5. Tote Bag")
            bag_choice = input("Enter your choice: ")
            bag_class = class_mapper[bag_choice]
            store.get_current_stock(bag_class)
            idx = int(input("Pick an index of the bag you want to buy: "))
            store.sell(store.stock[idx - 1])
            print("Thank you for buying!")
        
        elif choice == '3':
            store.get_current_stock()
        
        elif choice == '4':
            print("Exiting the store. Goodbye!")
            break
        
        else:
            print("Invalid choice! Please enter a valid option.")