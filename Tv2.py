x1 = 0
x3 = 0
class Tv:

    def num(self):
        print("Вы успешно включили телевизор")

    def v1(self):
        x = int(input('Выставте громкость'))
        if x > 100:
            print('громкость поставлена на макс.')
            x1 = 100
        elif x <= 100 and x >= 0:
            print('Громкость изменена')
            x1 = 0
            x1 = x
        elif x < 0:
            print('громкость поставлена на мин.')
            x1 = 0
        print('Щас стоит', x1, 'уровень звука')
    def v2(self):
        x2 = int(input('Изменит канал'))
        if x2 > 32:
            print('выше 32 не существует')
        elif x2 <=32 and x2 > 0:
            print('Канал изменён')
            x3 = x2
        elif x2<=0:
            print('ниже 1 канал ничего нет ')
        print('Щас включон', x3, 'канал')
 

def main():
    crit = Tv()

    choice = None  
    while choice != "0":
        print \
        ("""
        Мой Телевизор
    
        0 - Выйти
        1 - Включить телевизор
        2 - Изменить звук
        3 - Изменить канал
        """)
    
        choice = input("Ваш выбор: ")
        print()

        if choice == "0":
            print("До свидания.")

        elif choice == "1":
            crit.num()
        
        elif choice == "2":
            crit.v1()
         
        elif choice == "3":
            crit.v2()

        else:
            print("Извините, в меню нет пункта", choice)
    
main()