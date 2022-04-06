class Car:
    def __init__(self):
        self.wheels = 'wheels'

    def drive(self):
        print("drive")


if __name__ == '__main__':
    mycar = Car()
    hasattr(mycar, "wheels") # True
    hasattr(mycar, "drive") # True

    getattr(mycar, "wheels") # 'wheels'
    getattr(mycar, "drive") # 'drive'