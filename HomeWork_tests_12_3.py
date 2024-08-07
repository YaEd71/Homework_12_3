import unittest

class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5

    def __str__(self):
        return self.name

class RunnerTest(unittest.TestCase):

    def test_walk(self): # Правильность расчета дистанции при ходьбе
        runner = Runner("Alice")
        for _ in range(10):
            runner.walk()
        self.assertEqual(runner.distance, 50)

    def test_run(self): # Правильность расчета дистанции при беге
        runner = Runner("Bob")
        for _ in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100)

    def test_challenge(self): # Различие в дистанции между бегом и ходьбой
        runner1 = Runner("Charlie")
        runner2 = Runner("David")
        for _ in range(10):
            runner1.run()
            runner2.walk()
        self.assertNotEqual(runner1.distance, runner2.distance)

class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name

class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers

class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = {} # - словарь для хранения результатов всех тестов.

# Cоздаем трех бегунов с заданными именами и скоростями.
    def setUp(self):
        self.usain = Runner("Усэйн", 10)
        self.andrey = Runner("Андрей", 9)
        self.nick = Runner("Ник", 3)

# Cоздаем три тестовых метода с дистанцией 90 и соответствующими участниками.:
    def test_usain_and_nick(self):
        tournament = Tournament(90, self.usain, self.nick)
        results = tournament.start()  # Запускаем метод start()
        self.assertEqual(str(results[2]), "Ник")  #Проверяем, что последний финишировавший - это Ник.
        self.__class__.all_results["Усэйн и Ник"] = {k: str(v) for k, v in results.items()} # Сохраняем результаты.

    def test_andrey_and_nick(self):
        tournament = Tournament(90, self.andrey, self.nick)
        results = tournament.start()
        self.assertEqual(str(results[2]), "Ник")
        self.__class__.all_results["Андрей и Ник"] = {k: str(v) for k, v in results.items()}

    def test_usain_andrey_and_nick(self):
        tournament = Tournament(90, self.usain, self.andrey, self.nick)
        results = tournament.start()
        self.assertEqual(str(results[3]), "Ник")
        self.__class__.all_results["Усэйн, Андрей и Ник"] = {k: str(v) for k, v in results.items()}

# Изменили существующие тесты, чтобы они проверяли правильный порядок финиширования бегунов.
# Проверяем, что бегуны финишируют в правильном порядке на более длинной дистанции.
    def test_correct_finishing_order(self):
        tournament = Tournament(100, self.usain, self.andrey, self.nick)
        results = tournament.start()
        self.assertEqual([str(runner) for runner in results.values()], ["Усэйн", "Андрей", "Ник"])

# Проверка ситуации, когда у двух бегунов одинаковая скорость.
    def test_equal_speed_runners(self):
        runner1 = Runner("Бегун1", 5)
        runner2 = Runner("Бегун2", 5)
        tournament = Tournament(50, runner1, runner2)
        results = tournament.start()
        self.assertEqual(len(results), 2)
        self.assertIn(str(runner1), [str(v) for v in results.values()])
        self.assertIn(str(runner2), [str(v) for v in results.values()])

# Проверка корректности работы на короткой дистанции.
    def test_very_short_distance(self):
        tournament = Tournament(10, self.usain, self.andrey, self.nick)
        results = tournament.start()
        self.assertEqual(len(results), 3)
        self.assertEqual([str(runner) for runner in results.values()], ["Усэйн", "Андрей", "Ник"])

    @classmethod
    def tearDownClass(cls):
        for test_name, results in cls.all_results.items():
            print(f"{test_name}: {results}")

if __name__ == '__main__':
    unittest.main()

# Декоратор, который будет пропускать тесты, если is_frozen = True.
def skip_if_frozen(test_method):
    def wrapper(self):
        if self.is_frozen:
            raise unittest.SkipTest('Тесты в этом кейсе заморожены')
        return test_method(self)
    return wrapper

# Модифицируем RunnerTest
class ModifiedRunnerTest(RunnerTest):
    is_frozen = False

# Применяем декоратор ко всем тестовым методам
    @skip_if_frozen
    def test_walk(self):
        super().test_walk()

    @skip_if_frozen
    def test_run(self):
        super().test_run()

    @skip_if_frozen
    def test_challenge(self):
        super().test_challenge()

# Модифицируем TournamentTest
class ModifiedTournamentTest(TournamentTest):
    is_frozen = True

# Применяем декоратор ко всем тестовым методам
    @classmethod
    def setUpClass(cls):
        super().setUpClass()

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()

    @skip_if_frozen
    def setUp(self):
        super().setUp()

    @skip_if_frozen
    def test_usain_and_nick(self):
        super().test_usain_and_nick()

    @skip_if_frozen
    def test_andrey_and_nick(self):
        super().test_andrey_and_nick()

    @skip_if_frozen
    def test_usain_andrey_and_nick(self):
        super().test_usain_andrey_and_nick()

    @skip_if_frozen
    def test_correct_finishing_order(self):
        super().test_correct_finishing_order()

    @skip_if_frozen
    def test_equal_speed_runners(self):
        super().test_equal_speed_runners()

    @skip_if_frozen
    def test_very_short_distance(self):
        super().test_very_short_distance()

