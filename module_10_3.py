import threading
import time
import random


class Bank():
    def __init__(self, balance=0):
        self.balance = balance
        self.lock = threading.Lock()

    def deposit(self):
        money = random.randint(50,500)
        self.balance += money
        print(f'Пополнение на {money} руб, Баланс: {self.balance} руб')
        if self.balance >= 500 and self.lock.locked():
            self.lock.release()
        time.sleep(0.001)

    def take(self):
        money = random.randint(50, 500)
        print(f'Запрос  на {money} руб')
        if self.balance >= money:
            self.balance -= money
            print(f'Снятие {money} руб, Баланс: {self.balance} руб')
            print(self.lock.locked(), self.balance)
        else:
            print('Запрос отклонен')
            self.lock.acquire()
            print(self.lock.locked(), self.balance)
        time.sleep(0.001)

bk = Bank()
for i in range(100):

    th1 = threading.Thread(target=Bank.deposit, args=(bk,))
    th2 = threading.Thread(target=Bank.take, args=(bk,))

    th1.start()
    th2.start()

    th1.join()
    th2.join()

print(f"Итоговый баланс {bk.balance}")