from models.FoodMenu import FoodMenu
from models.FoodItems import FoodItem
from models.Restaurant import Restaurant

class FoodManager:

    def __init__(self):
        self.Restaurants = self.__prepareRestaurants()


    def __prepareFoodItems(self):
        item1 = FoodItem("Biriyani", 4.4, 120, "***")
        item2 = FoodItem("shawarma", 4.5, 100, "**")
        item3 = FoodItem("parotta", 4.3, 90, "****")
        item4 = FoodItem("Grill", 4.1, 150, "****")
        item5 = FoodItem("Noodles", 4.2, 170, "***")
        return [item1, item2, item3, item4, item5]

    def __prepareFoodMenus(self):
        FoodItems = self.__prepareFoodItems()
        menu1 = FoodMenu("Veg")
        menu1.FoodItems = [FoodItems[0]]
        menu2 = FoodMenu("NonVeg")
        menu2.FoodItems = [FoodItems[1],FoodItems[2],FoodItems[3]]
        menu3 = FoodMenu("Chinese")
        menu3.FoodItems = [FoodItems[4]]
        return [menu1, menu2, menu3]

    def __prepareRestaurants(self):
        FoodMenus = self.__prepareFoodMenus()
        res1 = Restaurant("A2B", 4.0, "chennai", 10)
        res1.FoodMenus = [FoodMenus[0]]
        res2 = Restaurant("SS", 4.4, "coimbatore", 15)
        res2.FoodMenus = [FoodMenus[0], FoodMenus[1],FoodMenus[2]]
        res3 = Restaurant("KFC", 4.1, "Banglore", 10)
        res3.FoodMenus = [FoodMenus[2]]
        return [res1, res2, res3]

    def FindRestaurant(self, name):
        for res in self.Restaurants:
            if res.Name == name:
                return res


