class Critter:
    "Бёрнли"
    total = 0

    def status():
        print("Общее число зверюшек", Critter.total)

    def __init__(self, name):
        self.__name = name
        print('Зверюшка появилась')
        Critter.total += 1

    @property
    def name(self):
        return self.__name

def main():
    crit_name1 = input("Как вы назовете свою зверюшку: ")
    crit = Critter(crit_name1)
    crit_name2 = input("Как вы назовете свою зверюшку: ")
    crit = Critter(crit_name2)
    crit_name3 = input("Как вы назовете свою зверюшку: ")
    crit = Critter(crit_name3)
    crit_name4 = input("Как вы назовете свою зверюшку: ")
    crit = Critter(crit_name4)
    crit_name5 = input("Как вы назовете свою зверюшку: ")
    crit = Critter(crit_name5)
    crit_name6 = input("Как вы назовете свою зверюшку: ")
    crit = Critter(crit_name6)
    crit_name7 = input("Как вы назовете свою зверюшку: ")
    crit = Critter(crit_name7)
    crit_name8 = input("Как вы назовете свою зверюшку: ")
    crit = Critter(crit_name8)
    crit_name9 = input("Как вы назовете свою зверюшку: ")
    crit = Critter(crit_name9)
    crit_name10 = input("Как вы назовете свою зверюшку: ")
    crit = Critter(crit_name10)
    Critter.status()
    print(crit_name1.total)
main()
