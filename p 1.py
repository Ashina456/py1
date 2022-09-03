import random

class Student:

    def __init__(self, name):
        self.name = name
        self.happiness = 50
        self.progress = 0
        self.alive = True

    def study(self):
        print("вчимося")
        self.progress += 0.25
        self.happiness -= 3

    def sleep(self):
        print("спимо")
        self.happiness +=3

    def chill(self):
        print("chill")
        self.happiness += 5
        self.progress -= 0.1

    def is_alive(self):
        if self.progress < -0.5:
            print("BAN")
            self.alive = False
        elif self.happiness <= 0:
            print(":(")
            self.alive = False
        elif self.progress > 5:
            print("екстерн")
            self.alive = False

    def end(self):
        print(f"щастя {self.happiness}")
        print(f"успішність {round(self.progress,2)}")

    def live(self, day):
        day = "день " + str(day) + " " + self.name + " життя"
        print(f"{day:=^50}")
        random_cude = random.randint(1, 3)
        if random_cude == 1:
            self.study()
        elif random_cude == 2:
            self.sleep()
        elif random_cude == 3:
            self.chill()
        self.end()
        self.is_alive()

dima = Student(name="dima")

for day in range(365):
    if dima.alive == False:
        break
    dima.live(day)