import unittest
import laba71 as code
import random
class TestProgramm(unittest.TestCase):
    def test_calc(self):
        matrix_test = code.create((8,6))
        for i in range(len(matrix_test)):
            list = matrix_test[i + 1]
            for number in list:
                if number >= 0:
                    index = list.index(number)
                    list[index] = 0
                    matrix_test.update({i + 1: list})
                else:
                    pass

        return matrix_test
        matrix = code.create((8,6))
        matrix = code.calc(matrix)
        self.assertEqual(matrix, matrix_test)