import unittest
from func_calcul import *


class Test_Calcul(unittest.TestCase):
    # def setUpClass(self):
    #     print('Запуск всех тестов из класса')

    def setUp(self):
        self.a = 10 #хочу задачь значения в начале теста
        self.b = 5
        print('Начало теста')

    def tearDown(self):
        print('Конец теста')

    def test_sum_two_number(self):
        self.assertEqual(sum_two_number(self.a, self.b), 15) #почему при запуске теста выводится результат в конце

    def test_difference(self):
        self.assertEqual(difference(self.a, self.b), 5)

    def test_multiply(self):
        self.assertEqual(multiply(self.a, self.b), 50)

    def test_share(self):
        self.assertEqual(share(self.a, self.b), 2)

    # def tearDownClass(self):
    #     print('Конец всех тестов из класса')




# if __name__ == '__main__':
#     unittest.main()



