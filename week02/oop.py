class car:
    def start(self):
        print("car is starting")
    def stop(self):
        print("car is stopping")

# car1 = car()
# car2 = car()
# car1.start()
# car2.start()
# car1.stop()
# car2.stop()

class bmw:
    def info(self, color, model):
        self.color = color
        self.model = model

cars = bmw()
cars.info("red", 203)
print(cars.color)
print(cars.model)

class lams:
    def __init__(self, size, color, model, ws):
        self.size = size
        self.color = color
        self.model = model
        self.ws = ws
ys = lams(100, "sd", 20, 100)
print(ys.size)
print(ys.color)




