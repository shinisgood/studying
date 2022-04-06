from functools import reduce   # 파이썬 3에서는 써주셔야 해요  

def mul5(x):
    return 5*x


if __name__ == '__main__':
    mul5(5)
    (lambda x,y : x+y)(1,2) # 3
    list(map(lambda x: x + 1, [1,2,3,4,5])) # [2, 3, 4, 5, 6]
    list(filter(lambda x: x > 1, [1,2,3,4,5])) # [2, 3, 4, 5]
    reduce(lambda x, y: x + y, [0, 1, 2, 3, 4]) # 10
    
