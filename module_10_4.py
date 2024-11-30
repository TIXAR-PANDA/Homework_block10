# Очереди для обмена данными между потоками.

import threading
import random
import time
from queue import Queue


class Table:
    """
    number - номер стола
    guest - гость, который сидит за этим столом (по умолчанию None)
    """
    def __init__(self, number):
        self.number = number
        self.guest = None

class Guest(threading.Thread):
    """ name - имя гостя"""

    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        time.sleep(random.randint(3, 10))


class Cafe:
    """
    queue - очередь (объект класса Queue)
    tables - столы в этом кафе
    """
    def __init__(self, *tables):
        self.queue = Queue()
        self.tables = list(tables)

    def guest_arrival(self, *guests):
        for guest in guests:
            table = self.free_table()
            if table:
                table.guest = guest
                guest.start()
                print(f'Клиент {guest.name} сел за стол номер {table.number}')
            else:
                self.queue.put(guest)
                print(f'{guest.name} в очереди')

    def discuss_guests(self):
        while not self.queue.empty() or self.gues_seated():
            for table in self.tables:
                if table.guest and not table.guest.is_alive():
                    print(f'Клиент {table.guest.name} покушал и ушёл')
                    print(f'Стол номер {table.number} свободен')
                    table.guest = None

                if not self.queue.empty() and table.guest is None:
                    next_guest = self.queue.get()
                    table.guest = next_guest
                    next_guest.start()
                    print(f'Клиент {next_guest.name} вышел из очереди и сел за стол номер {table.number}')

    def free_table(self):
        for table in self.tables:
            if table.guest is None:
                return table
        return None

    def gues_seated(self):
        return any(table.guest is not None for table in self.tables)

# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = [
'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()
