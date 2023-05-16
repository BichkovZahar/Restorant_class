class FoodItem:
    def __init__(self , name , description, price):
        self.name = name
        self.description = description
        self.price = price
    def __str__(self):
        pass
class Menu:
    def __init__(self):
        self.menu = []
    def add_menu(self , food):
        self.menu.append(food)
    def remove_menu(self , food):
        self.menu.remove(food)
    def view_menu(self):
        for dict in self.menu:
            print(f"| Назва: {dict.name} | Состав: ({dict.description}) | Цена: {dict.price}")
class Order:
    def __init__(self):
        self.menu_1 = []
    def add_food(self , food):
        self.menu_1.append(food)
    def remove_food(self, food):
        if len(self.menu_1) == 0:
          print("Ви нічого не замовили")
        else:
          self.menu_1.remove(food)
    def suma_food(self):
        suma = 0
        if len(self.menu_1):
            print("Ви нічого не замовили")
        else:
            for dictionary in self.menu_1:
                suma += dictionary.price
class Restoraunt:
    def __init__(self):
        self.menu = Menu()
        self.foods = []
    def add_foods(self , food):
        self.foods.append(food)
    def remove_foods(self , food):
        self.foods.remove(food)
    def finish(self):
        total_price = 0
        print("                      Розрахунок")
        for suma in self.foods:
            total_price += suma.price
            print(f"{suma.name} -> {suma.price}")
        print(f"Сума: {total_price}")
print("                          Меню      ")
food_item1 = FoodItem("Caesar" , "Egg , crackers , lettuce croutons" , 300)
food_item2 = FoodItem("Steak" , "Meat , spices" , 600)
food_item3 = FoodItem("Okroshka" , "Sausage , greenery , cucumber", 250)


#Виводимо меню
menu = Menu()
menu.add_menu(food_item1)
menu.add_menu(food_item2)
menu.add_menu(food_item3)
menu.view_menu()

#робимо заказ
order = Order()
order.add_food(food_item3)
order.add_food(food_item1)

restoran = Restoraunt()
restoran.add_foods(food_item3)
restoran.add_foods(food_item1)
restoran.finish()

with open ("info_restourant.txt" , "w") as file:
    file.write("    Check")
    total_price = 0
    for i in order.menu_1:
        file.write(f"\n| {i.name} -> {i.price}")
        total_price += i.price
    file.write(f"\nSuma: {total_price}")