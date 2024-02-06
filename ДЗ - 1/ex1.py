class Soda:
    def __init__(self, addition=None):
        self.addition = addition

    def show_my_drink(self):
        if isinstance(self.addition, str):
            print(f'Газировка и {self.addition}')
        else:
            print('Обычная газировка')


drink1 = Soda()
drink2 = Soda('малина')
drink3 = Soda(5)

drink1.show_my_drink()
drink2.show_my_drink()
drink3.show_my_drink()
