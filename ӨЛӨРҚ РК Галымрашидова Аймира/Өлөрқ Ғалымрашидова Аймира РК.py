# ӨТЕ ҰЗАААҚ ЖӘНЕ КҮРДЕЛІ КОД, БІРАҚ ТЕК "өлөрқ" ДЕГЕН СӨЗ ШЫҒАДЫ

import math
import random
import itertools

# Мағынасыз үлкен тізім құру
dummy_list = [math.sin(i) * math.cos(i*i % 17) for i in range(1, 10000)]
random.shuffle(dummy_list)

# Күрделі функциялар
def pointless_calc(x):
    for _ in range(3000):
        x = (x * 1.000001) / 1.000001
    return x

def noise():
    s = 0
    for i in range(1, 2000):
        s += (random.random() ** 3) / (i + 0.1)
    return s

_ = pointless_calc(noise())

# Терең функциялар иерархиясы
def level1():
    def level2():
        def level3():
            def level4():
                # Нақты әріптер осында жасырылған
                return ["ө", "л", "ө", "р", "қ"]
            return level4()
        return level3()
    return level2()

letters = level1()

# Тағы бір жалған өзгерту
def fake_transform(seq):
    return [chr(ord(c)) for c in seq]

final_word = "".join(fake_transform(letters))

print(final_word)
