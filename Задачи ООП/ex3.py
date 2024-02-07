class Recipe:
    def __init__(self, name, ingredients):
        self.name = name
        self.ingredients = ingredients

    def print_ingredients(self):
        print("Список продуктов для рецепта '{}':".format(self.name))
        for ingredient in self.ingredients:
            print("- " + ingredient)

    def cook(self):
        print("Готовится блюдо по рецпту '{}'...".format(self.name))
        print("Блюдо '{}' готово!".format(self.name))

recipe = Recipe ("Салат Цезарь", ["Курица", "Салатный лист", "Сухарики", "Пармезан", "Соус Цезарь"])

recipe.print_ingredients()

recipe.cook()

cake = Recipe("Кекс", ["Мука", "Яйца", "Молоко", "Сахар", "Сливочное масло", "Соль", "Ванилин"])

cake.print_ingredients()

cake.cook()