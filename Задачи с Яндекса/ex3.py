class RedButton:
    def __init__(self):
        self.count = 0

    def click(self):
        self.count += 1
        print("Тревога!")

    def getCount(self):
        return self.count

button = RedButton()

button.click()
button.click()

count = button.getCount()

print(count)