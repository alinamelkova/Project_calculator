import pytest
from func_calcul import *


@pytest.fixture(scope='session')
def create_ab():
    print('Начало теста')
    a = 10
    b = 5
    yield
    print('Конец теста')


class Test_Calcul():
    # def setUp(self, a, b):
    #     print('Начало теста')
    #     a = 10
    #     b = 5
    #
    # def terndown(self):
    #     print('Конец теста')

    def test_sum_two_number(self, a, b):
        assert sum_two_number(a, b) == 15

    def test_difference(self, a, b):
        assert difference(a, b) == 5

    def test_multiply(self, a, b):
        assert multiply(a, b) == 50

    def test_share(self, a, b):
        assert share(a, b) == 2
