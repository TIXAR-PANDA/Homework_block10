# блокировки потоков
import random
import time
import threading
class Bank:
    """
    balance - баланс банка (int)
    lock - объект класса Lock для блокировки потоков.
    """

    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self):
        for i in range(100): # Будет совершать 100 транзакций пополнения средств.
            addition = random.randint(50, 500) # пополнение - случайное целое число от 50 до 500.
            self.balance += addition  # пополнили баланс
   # если баланс больше или равен 500 и замок lock заблокирован - lock.locked(),
            if self.balance >= 500 and self.lock.locked():
                # то разблокировать его методом release.
                self.lock.release()
    # После увеличения баланса должна выводится строка
            # "Пополнение: <случайное число>. Баланс: <текущий баланс>".
            print(f'Пополнение: {addition}. Баланс: {self.balance}')
            time.sleep(0.001)

    def take(self):
        for i in range(100): # Будет совершать 100 транзакций снятия.
            removing = random.randint(50, 500) # Снятие - случайное целое число от 50 до 500.
    # В начале должно выводится сообщение "Запрос на <случайное число>".
            print(f'Запрос на {removing}')
    # Далее производится проверка: если случайное число меньше или равно текущему балансу,
            if self.balance >= removing:
    # то произвести снятие, уменьшив balance
                self.balance -= removing

    # и вывести на экран "Снятие: <случайное число>. Баланс: <текущий баланс>".
                print(f'Снятие: {removing}. Баланс: {self.balance}')
                time.sleep(0.001)
            else: # Если случайное число оказалось больше баланса,
                # то вывести строку "Запрос отклонён, недостаточно средств"
                print(f'Запрос отклонён, недостаточно средств')
                time.sleep(0.001)
                # и заблокировать поток методом acquire.
                self.lock.acquire()



bk = Bank()

th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
