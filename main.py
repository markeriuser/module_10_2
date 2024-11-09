import time
from threading import Thread


class Knight(Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power
        self.enemies = 100  # Общее количество врагов
        self.days = 0  # Количество дней сражения

    def run(self):
        print(f"{self.name}, на нас напали!")
        while self.enemies > 0:
            time.sleep(1)  # Задержка 1 секунда (1 день сражения)
            self.days += 1
            self.enemies -= self.power
            if self.enemies < 0:
                self.enemies = 0
            print(f"{self.name}, сражается {self.days} день(дня)..., осталось {self.enemies} воинов.")

        print(f"{self.name} одержал победу спустя {self.days} дней(дня)!")


# Создаем экземпляры рыцарей
first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight('Sir Galahad', 20)

# Запускаем потоки
first_knight.start()
second_knight.start()

# Ждем завершения битв
first_knight.join()
second_knight.join()

print("Все битвы закончились!")
