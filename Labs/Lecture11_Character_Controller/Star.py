class Star:

    type = 'Star'
    x = 100

    def change():
        x = 200
        print('x is ', x)

print('x IS ', Star.x)
Star.change()
print('x IS ', Star.x)

star = Star()
print('x IS ', star.x)
star.change()# 인자가 없는데 클래스 내의 함수를 실행하려 해서 문제