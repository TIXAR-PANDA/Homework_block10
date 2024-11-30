# блокировки потоков
import random
import time
import threading
class Bank:
    """
    balance - баланс банка (int)
    """

    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self):
        for i in range(100):
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            addition = random.randint(50, 500)
            self.balance += addition
            print(f'Пополнение: {addition}. Баланс: {self.balance}')
            time.sleep(0.001)

    def take(self):
        for i in range(100):
            removing = random.randint(50, 500)
            print(f'Запрос на {removing}')
            if self.balance >= removing:
                self.balance -= removing
                print(f'Снятие: {removing}. Баланс: {self.balance}')
            else:
                print(f'Запрос отклонён, недостаточно средств')
                self.lock.acquire()
            time.sleep(0.001)


bk = Bank()

th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')