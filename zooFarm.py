import random
class Critter:
    """Виртуальный питомец"""
    total = 0

    @staticmethod   
    def status():
        print("Общее число зверюшек", Critter.total)

    def __init__(self, name, hunger = 0, boredom = 0):
        self.__name = name
        self.hunger = random.randint(0, 16)
        self.boredom = random.randint(0, 16)
        Critter.total += 1

    def __str__(self):
        ans = 'Объект класса Critter\n'
        ans += 'имя: ' + self.name + '\n'
        return ans
    
    def __pass_time(self):
        self.hunger += 1
        self.boredom += 1

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        if new_name == "":
            print("Имя зверушки не может быть пустой строкой.")
        else:
            self.__name = new_name
            print("Имя успешно изменено.")

    @property
    def mood(self):
        unhappiness = self.hunger + self.boredom
        if unhappiness < 5:
            m = "прекрасно"
        elif 5 <= unhappiness <= 10:
            m = "неплохо"
        elif 11 <= unhappiness <= 15:
            m = "не сказать чтобы хорошо"
        else:
            m = "ужасно"
        return m

    def talk(self):
        print("Меня зовут", self.name, 
              ", и сейчас я чувствую себя", self.mood)
        self.__pass_time()
        
    def number(self, number=-1):        
        while number<0:
          number=int(input('Сколько? '))
        return number 

    def eat(self, food = 4):
        print("Мррр...  Спасибо!")
        self.hunger -= food
        if self.hunger < 0:
            self.hunger = 0
        self.__pass_time()

    def play(self, fun = 4):
        print("Уиии!")
        self.boredom -= fun
        if self.boredom < 0:
            self.boredom = 0
        self.__pass_time()

def main():
    crit_name = input("Как в хотите назвать петуха?")
    cock = Critter(crit_name)
    crit_name = input("Как в хотите назвать кота? ")
    cat = Critter(crit_name)
    crit_name = input("Как в хотите назвать собаку? ")
    dog = Critter(crit_name)

    choice = None  
    while choice != "0":
        print \
        ("""
        Моя зверюшка
    
        0 - Выйти
        1 - Узнать о самочувствии зверюшки
        2 - Покормить зверюшку
        3 - Поиграть со зверюшкой
        """)
    
        choice = input("Ваш выбор: ")
        print()

        # выход
        if choice == "0":
            print("До свидания.")

        # беседа со зверюшкой
        elif choice == "1":
            cock.talk()
            cat.talk()
            dog.talk()
        
        # кормление зверюшки
        elif choice == "2":
            numb=Critter
            numb.number(self)
            cock.eat(numb)
            cat.eat(numb)
            dog.eat(numb)
         
        # игра со зверюшкой
        elif choice == "3":
            numb=Critter
            numb.number(self)
            cock.play(numb)
            cat.play(numb)
            dog.play(numb)
            print("Увиии")

        # непонятный пользовательский ввод
        else:
            print("Извините, в меню нет пункта", choice)
    
main()
