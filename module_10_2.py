# Потоки на классах.
import threading
import time
class Knight(threading.Thread):
    """
Атрибуты: name - имя рыцаря. (str)
          power - сила рыцаря. (int)
    """
    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power

    def run(self):
        print(f"{self.name}, на нас напали!")
        enemy_power = 100
        number_of_days = 0
        while enemy_power:
            number_of_days += 1
            enemy_power = enemy_power - self.power
            time.sleep(1)
            print(f"{self.name} сражается {number_of_days}-й день,"
                  f" осталось {enemy_power} воинов.")
        print(f"{self.name} одержал победу спустя {number_of_days} дней!")

first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad ", 20)
first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()

print('Все битвы закончились!')

