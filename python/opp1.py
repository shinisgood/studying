class Fridge:
    def __init__(self):
        self.isOpened = False
        self.foods = []
    
    def open(self):
        self.isOpened = True
        print ('냉장고 문을 열었어요...')
    
    def put(self, thing):
        if self.isOpened:
            self.foods.append(thing)
            print (f'냉장고 속에 {thing}이 들어갔네...')
        else:
            print ('냉장고 문이 닫혀있어서 못넣겠어요...')
    
    def close(self):
        self.isOpened = False
        print ('냉장고 문을 닫았어요...')

class Food:
    pass

if __name__ == '__main__':
    f = Fridge()
    apple = Food()
    elephant = Food()
    a='a'