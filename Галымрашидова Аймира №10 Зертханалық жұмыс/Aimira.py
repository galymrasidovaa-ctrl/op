import math


# ------------------ 1. Person / Student ------------------
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")


class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, ID: {self.student_id}")


student = Student("Aigerim", 21, "ST1023")
student.display_info()


# ------------------ 2. Employee / Manager ------------------
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display_info(self):
        print(f"Name: {self.name}, Salary: {self.salary} тг")


class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

    def display_info(self):
        print(f"Name: {self.name}, Salary: {self.salary} тг, Department: {self.department}")


manager = Manager("Dana", 450000, "IT бөлім")
manager.display_info()


# ------------------ 3. Animal / Dog ------------------
class Animal:
    def speak(self):
        print("This animal makes a sound.")


class Dog(Animal):
    def speak(self):
        print("The dog barks: Woof! Woof!")


a = Animal()
d = Dog()

a.speak()
d.speak()


# ------------------ 4. Vehicle / Car ------------------
class Vehicle:
    def move(self):
        print("This vehicle can move.")


class Car(Vehicle):
    def move(self):
        print("The car drives on the road.")


v = Vehicle()
c = Car()

v.move()
c.move()


# ------------------ 5. Shape / Circle / Rectangle ------------------
class Shape:
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


shapes = [Circle(5), Rectangle(4, 6)]

for shape in shapes:
    print("Area:", shape.area())


# ------------------ 6. Square / Triangle ------------------
class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2


class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


shapes2 = [Square(4), Triangle(6, 3)]

for shape in shapes2:
    print("Area:", shape.area())


# ------------------ 7. Building / House / Office ------------------
class Building:
    def area(self):
        pass


class House(Building):
    def __init__(self, rooms):
        self.rooms = rooms

    def area(self):
        return self.rooms * 20


class Office(Building):
    def __init__(self, floors):
        self.floors = floors

    def area(self):
        return self.floors * 150


buildings = [House(5), Office(3)]

for b in buildings:
    print("Total area:", b.area(), "м²")


# ------------------ 8. Teacher / Researcher / Professor ------------------
class Teacher:
    def role(self):
        print("Teaching students.")


class Researcher:
    def role(self):
        print("Conducting research.")


class Professor(Teacher, Researcher):
    def role(self):
        super().role()
        print("Also managing academic projects.")


p = Professor()
p.role()


# ------------------ 9. Employee / Leader / ProjectManager ------------------
class Employee:
    def duty(self):
        print("Completing daily tasks.")


class Leader:
    def duty(self):
        print("Leading the team.")


class ProjectManager(Employee, Leader):
    def duty(self):
        super().duty()
        print("Also coordinating multiple projects.")


pm = ProjectManager()
pm.duty()


# ------------------ 10. PoliceOfficer / Trainer / Chief ------------------
class PoliceOfficer:
    def work(self):
        print("Maintaining public safety.")


class Trainer:
    def work(self):
        print("Training new recruits.")


class Chief(PoliceOfficer, Trainer):
    def work(self):
        super().work()
        print("Also overseeing operations.")


chief = Chief()
chief.work()


# ------------------ 11. Chef / Artist / MasterChef ------------------
class Chef:
    def job(self):
        print("Cooking delicious meals.")


class Artist:
    def job(self):
        print("Creating artistic presentations.")


class MasterChef(Chef, Artist):
    def job(self):
        super().job()
        print("Also innovating new recipes.")


mc = MasterChef()
mc.job()
