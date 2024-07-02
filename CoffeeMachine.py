class Coffee:
  def __init__(self, name, water, milk, coffee_beans, price):
      self.name = name
      self.water = water
      self.milk = milk
      self.coffee_beans = coffee_beans
      self.price = price

  def __str__(self):
      return f"{self.name} - ${self.price:.2f}"

class Inventory:
    def __init__(self, water, milk, coffee_beans, money=0):
        self.water = water
        self.milk = milk
        self.coffee_beans = coffee_beans
        self.money = money

    def check_ingredients(self, coffee):
        if self.water < coffee.water:
            return "Not enough water."
        if self.milk < coffee.milk:
            return "Not enough milk."
        if self.coffee_beans < coffee.coffee_beans:
            return "Not enough coffee beans."
        return "Ingredients are sufficient."

    def use_ingredients(self, coffee):
        self.water -= coffee.water
        self.milk -= coffee.milk
        self.coffee_beans -= coffee.coffee_beans
        self.money += coffee.price

class Machine:
    def __init__(self):
        self.inventory = Inventory(1000, 500, 200)
        self.menu = [
            Coffee("Espresso", 50, 0, 18, 1.50),
            Coffee("Latte", 200, 150, 24, 2.50),
            Coffee("Cappuccino", 250, 100, 24, 3.00),
        ]

    def display_menu(self):
        print("Available Coffees:")
        for i, coffee in enumerate(self.menu, 1):
            print(f"{i}. {coffee}")

    def select_coffee(self, choice):
        if 1 <= choice <= len(self.menu):
            return self.menu[choice - 1]
        else:
            return None

    def make_coffee(self, coffee):
        if coffee:
            status = self.inventory.check_ingredients(coffee)
            if status == "Ingredients are sufficient.":
                self.inventory.use_ingredients(coffee)
                print(f"Enjoy your {coffee.name}!")

            else:
                print(status)
        else:
            print("Invalid choice. Please select a valid coffee.")

    def show_inventory(self):
        print(f"Inventory: Water={self.inventory.water}ml, Milk={self.inventory.milk}ml, Coffee Beans={self.inventory.coffee_beans}g, Money=${self.inventory.money:.2f}")
