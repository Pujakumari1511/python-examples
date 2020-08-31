class Wing():
    def __init__(self, ratio):
       self.ratio = ratio

    def fly(self):
        if self.ratio > 1:
            print("Weee this is fun")
        elif self.ratio == 1:
            print("This is hard work, but i am flying.")
        else:
            print("I think I will just walk.")


class Duck:

    def __init__(self):
        self._wing = Wing(0.8)

    def walk(self):
        print("waddle, waddle, waddle")

    def swim(self):
        print("come on it, the water's lovely")

    def quack(self):
        print("Quack, quack")

    def fly(self):
        self._wing.fly()

class Penguin:

    def walk(self):
        print("waddle, waddle, I waddle too")

    def swim(self):
        print("come on it, but its' a bit chilly this far south")

    def quack(self):
        print("Are you 'avin' a larf? I am a penguin.")

# def test_duck(duck):
#     duck.walk()
#     duck.swim()
#     duck.quack()

if __name__ == "__main__":
    donald = Duck()
    donald.fly()

    # percy = Penguin()
    # test_duck(percy)