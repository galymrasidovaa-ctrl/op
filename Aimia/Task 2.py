# Strategy базалық класы
class DiscountStrategy:
    def apply(self, price):
        """Бағаны стратегияға сәйкес өзгертеді"""
        raise NotImplementedError("Бұл әдісті ұрпақ класс жүзеге асыруы тиіс.")

# Конкретті стратегиялар
class NoDiscount(DiscountStrategy):
    def apply(self, price):
        return price

class PercentageDiscount(DiscountStrategy):
    def __init__(self, percent):
        self.percent = percent

    def apply(self, price):
        return price * (1 - self.percent / 100)

class FixedDiscount(DiscountStrategy):
    def __init__(self, amount):
        self.amount = amount

    def apply(self, price):
        return max(0, price - self.amount)

# Контекст функциясы
def calculate_total(price, strategy: DiscountStrategy):
    return strategy.apply(price)


# Демонстрация
price = 200

# No discount
no_discount = NoDiscount()
print("No Discount:", calculate_total(price, no_discount))  # 200

# 15% Discount
percent_discount = PercentageDiscount(15)
print("15% Discount:", calculate_total(price, percent_discount))  # 170.0

# Fixed discount $50
fixed_discount = FixedDiscount(50)
print("Fixed $50 Discount:", calculate_total(price, fixed_discount))  # 150

# Стратегияны runtime-те ауыстыру
strategy = NoDiscount()
print("Initial:", calculate_total(price, strategy))  # 200

strategy = PercentageDiscount(10)
print("Switched to 10% Discount:", calculate_total(price, strategy))  # 180.0

strategy = FixedDiscount(80)
print("Switched to $80 Discount:", calculate_total(price, strategy))  # 120
