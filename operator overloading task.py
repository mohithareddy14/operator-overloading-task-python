# OPERATOR OVERLOADING IN PYTHON
# Assignment: Operator Overloading Practice


# 1. BOOK
class Book:
    def __init__(self, pages):
        self.pages = pages

    def __add__(self, other):
        return Book(self.pages + other.pages)

    def __str__(self):
        return str(self.pages) + " pages"


book1 = Book(200)
book2 = Book(150)

book3 = book1 + book2

print("1. Book")
print("Book 1:", book1)
print("Book 2:", book2)
print("Total Pages:", book3)
print()


# 2. EMPLOYEE
class Employee:
    def __init__(self, salary):
        self.salary = salary

    def __gt__(self, other):
        return self.salary > other.salary


emp1 = Employee(50000)
emp2 = Employee(40000)

print("2. Employee")
print("Employee 1 Salary:", emp1.salary)
print("Employee 2 Salary:", emp2.salary)
print("Employee 1 > Employee 2:", emp1 > emp2)
print()


# 3. TEMPERATURE
class Temperature:
    def __init__(self, value):
        self.value = value

    def __sub__(self, other):
        return self.value - other.value


temp1 = Temperature(35)
temp2 = Temperature(20)

difference = temp1 - temp2

print("3. Temperature")
print("Temperature 1:", temp1.value, "°C")
print("Temperature 2:", temp2.value, "°C")
print("Temperature Difference:", difference, "°C")
print()


# 4. RECTANGLE
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def __mul__(self, other):
        return self.area() * other.area()


rect1 = Rectangle(10, 5)
rect2 = Rectangle(4, 3)

result = rect1 * rect2

print("4. Rectangle")
print("Rectangle 1 Area:", rect1.area())
print("Rectangle 2 Area:", rect2.area())
print("Product of Areas:", result)
print()


# 5. TIME
class Time:
    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes

    def __add__(self, other):
        total_minutes = self.minutes + other.minutes
        total_hours = self.hours + other.hours

        # Normalize minutes
        total_hours += total_minutes // 60
        total_minutes = total_minutes % 60

        return Time(total_hours, total_minutes)

    def __str__(self):
        return f"{self.hours} hours {self.minutes} minutes"


time1 = Time(2, 50)
time2 = Time(1, 40)

time3 = time1 + time2

print("5. Time")
print("Time 1:", time1)
print("Time 2:", time2)
print("Total Time:", time3)
print()


# 6. SHOPPING CART
class ShoppingCart:
    def __init__(self, prices):
        self.prices = prices

    def __add__(self, other):
        return ShoppingCart(self.prices + other.prices)

    def total(self):
        return sum(self.prices)

    def __str__(self):
        return str(self.prices)


cart1 = ShoppingCart([100, 200, 150])
cart2 = ShoppingCart([300, 250])

cart3 = cart1 + cart2

print("6. Shopping Cart")
print("Cart 1:", cart1)
print("Cart 2:", cart2)
print("Combined Cart:", cart3)
print("Total Price:", cart3.total())
print()


# 7. DISTANCE
class Distance:
    def __init__(self, meters):
        self.meters = meters

    def __add__(self, other):
        return Distance(self.meters + other.meters)

    def __sub__(self, other):
        return Distance(self.meters - other.meters)

    def __eq__(self, other):
        return self.meters == other.meters

    def __str__(self):
        return str(self.meters) + " meters"


distance1 = Distance(500)
distance2 = Distance(300)
distance3 = Distance(500)

print("7. Distance")
print("Distance 1:", distance1)
print("Distance 2:", distance2)

print("Addition:", distance1 + distance2)
print("Subtraction:", distance1 - distance2)
print("Distance 1 == Distance 2:", distance1 == distance2)
print("Distance 1 == Distance 3:", distance1 == distance3)
print()


# 8. VECTOR
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        # Dot Product
        return (self.x * other.x) + (self.y * other.y)

    def __str__(self):
        return f"({self.x}, {self.y})"


vector1 = Vector(3, 4)
vector2 = Vector(2, 5)

print("8. Vector")
print("Vector 1:", vector1)
print("Vector 2:", vector2)
print("Addition:", vector1 + vector2)
print("Subtraction:", vector1 - vector2)
print("Dot Product:", vector1 * vector2)
    
