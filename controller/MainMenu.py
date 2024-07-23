from controller.FoodManager import FoodManager
from models.Cart import Cart
class MainMenu:
    __Options={1: "Show Restaurants", 2: "ShowFoodItems", 3: "Search Restaurant",  4: "Search FoodItem", 5: "Logout"}

    def __init__(self):
        self.__FoodManager = FoodManager()

    def ShowRestaurants(self):
        for i,res in enumerate(self.__FoodManager.Restaurants,1):
           res.DisplayItem(i)
        choice = int(input("Please select the Restaurant: "))
        res = self.__FoodManager.Restaurants[choice]
        self.ShowFoodMenus(res.FoodMenus)

    def ShowFoodItems(self, foodItems=None):
        if foodItems is not None:
            for i,foodItem in enumerate(foodItems,1):
                foodItem.DisplayItem(i)
            choices = list(map(int,input("Please choose your food items (eg 1,2) : ").split(',')))
            cart = Cart(foodItems,choices)
            cart.ProcessOrder(foodItems)

        else:
            pass

    def SearchRestaurant(self):
        resName = input("Enter Restaurant Name: ")
        res = self.__FoodManager.FindRestaurant(resName)

        if res is not None:
            print("Restaurant found...")
            print(f"Name: {res.Name}, Rating :{res.Rating}")
            self.ShowFoodMenus(res.FoodMenus)
        else:
            print(f"f No Restaurant found on the name{resName}")


    def SearchFooditems(self):
        pass

    def ShowFoodMenus(self,menus):
        print("\n\n List of Menus Availabale")
        for i,menu in enumerate(menus,1):
            menu.DisplayItem(i)
        choice = int(input("Please choose Menu: "))
        fooditems = menus[choice-1].FoodItems
        self.ShowFoodItems(fooditems)

    def LogOut(self):
        exit()
    def Start(self):
        while True:
            for option in MainMenu.__Options:
                print(f"{option}.{MainMenu.__Options[option]}", end=" ")
            print()
            try:
                choice=int(input("Enter your Choice: "))
                value = MainMenu.__Options[choice].replace(" ","")
                getattr(self, value)()
            except (ValueError, KeyError):
                print("invalid choice")

