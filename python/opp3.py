class Book:
    ## 데이터 세팅 초기화 하는방법
    def setData(self, title, price, author):
        self.title = title
        self.price = price
        self.author = author

    def printData(self):
        print('제목 : ', self.title)
        print('가격 : ', self.price)
        print('저자 : ', self.author)

    def __init__(self, title, price, author):
        self.setData(title, price, author)
        print('책 객체를 새로 만들었어요~')
        
    ## __repr__ 메서드 (프린팅)
    def __repr__(self):
        return self.title


class Shape:
    area = 0
    ## 메서드 (덧셈)
    def __add__(self, other):
        return self.area + other.area

    # __cmp__ 메서드 (비교)
    def __cmp__(self, other):
        if self.area < other.area :
            return f'{other.area}이 더 커염'
        elif self.area == other.area :
            return f'또까타여'
        else :
            return f'{other.area}이 더 작아염'


if __name__ == '__main__':
    b3 = Book('나두 좀 줘', '100원', '쥐벼룩')  # 책 객체를 새로 만들었어요~  
    print(b3) # '나두 좀 줘'

    ## 메서드 (덧셈)
    a = Shape()
    a.area = 20
    b = Shape()
    b.area = 10
    a + b # 30
    a.__add__(b) # 30
    
    print('a가 더 넓어요~') if a.area > b.area  else print('b가 더 넓어요~') # a가 더 넓어요~


