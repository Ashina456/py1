import random


class Student:

    def __init__(self, name):
        self.name = name
        self.happiness = 50
        self.progress = 0
        self.money = 10
        self.alive = True

    def study(self):
        print("вчимося")
        self.progress += 0.25
        self.happiness -= 3

    def sleep(self):
        print("спимо")
        self.happiness += 3

    def chill(self):
        print("chill")
        self.happiness += 5
        self.progress -= 0.1
        self.money -= 2

    def work(self):
        print("працюю")
        self.money += 2

    def is_alive(self):
        if self.progress < -0.5:
            print("BAN")
            self.alive = False
        elif self.happiness <= 0:
            print(":(")
            self.alive = False
        elif self.progress > 15:
            print("екстерн")
            self.alive = False

    def end(self):
        print(f"щастя {self.happiness}")
        print(f"успішність {round(self.progress, 2)}")
        print(f"гроші {self.money}")

    def live(self, day):
        day = str(day) + " день " + "життя " + self.name
        print(f"{day:=^50}")
        random_cude = random.randint(1, 4)
        money = self.money
        progress = self.progress
        if random_cude == 1 or progress > 0.2:
            self.study()
        elif random_cude == 2:
            self.sleep()
        elif random_cude == 3 & money > 2:
            self.chill()
        elif random_cude == 4 or money < 4:
            self.work()
        self.end()
        self.is_alive()


dima = Student(name="dima")

for day in range(365):
    if dima.alive == False:
        break
    dima.live(day)