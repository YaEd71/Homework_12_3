import unittest
import HomeWork_tests_12_3


# Создаем TestSuite
test_suite = unittest.TestSuite()

# Добавляем тесты в TestSuite
test_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(HomeWork_tests_12_3.ModifiedRunnerTest))
test_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(HomeWork_tests_12_3.ModifiedTournamentTest))

# Создаем TextTestRunner
runner = unittest.TextTestRunner(verbosity=2)

if __name__ == '__main__':
    # Запускаем тесты
    result = runner.run(test_suite)