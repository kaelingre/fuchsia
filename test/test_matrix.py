import unittest

from   delirium.matrix import (
           alphabet, coefficient_low, degree_high, degree_low, new_Matrix, var)

eps, x = var("eps, x")

class Test(unittest.TestCase):
    def test_alphabet(t):
        with open('test/data/git_410') as f:
            m = new_Matrix(f)
        t.assertEqual(
            alphabet(m, x),
            set([x-1, x, x+1]))

    def test_coefficient_low(t):
        with open('test/data/henn_324') as f:
            m = new_Matrix(f)
        t.assertEqual(
            coefficient_low(m, 'x'),
            new_Matrix([0, 0, -1, 0]))

    def test_degree(t):
        # test 01
        with open('test/data/henn_324') as f:
            m = new_Matrix(f)
        t.assertEqual(degree_high(m, 'x'), 0)
        t.assertEqual(degree_low(m, 'x'), -2)
        # test 02
        with open('test/data/bar_ex1') as f:
            m = new_Matrix(f)
        t.assertEqual(degree_high(m, 'x'), 0)
        t.assertEqual(degree_low(m, 'x'), -9)

    def test_new_Matrix_from_file(t):
        with open('test/data/henn_324') as f:
            m = new_Matrix(f)
        t.assertEqual(m, new_Matrix([eps/x, 0, -1/x**2, eps/(1+x)]))

if __name__ == "__main__":
    unittest.main(verbosity=2)
