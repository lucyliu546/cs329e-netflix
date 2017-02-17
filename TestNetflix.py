#!/usr/bin/env python3

# -------
# imports
# -------
from Netflix import netflix_eval
from unittest import main, TestCase
from math import sqrt
from io import StringIO
from numpy import sqrt, square, mean, subtract

# -----------
# TestNetflix
# -----------

class TestNetflix (TestCase):

    # ----
    # eval
    # ----
    # customers must exist in probe data for unit tests to work

    def test_eval_1(self):
        r = StringIO("1:\n30878\n2647871\n1283744")
        w = StringIO()
        netflix_eval(r, w)
        self.assertEqual(
            w.getvalue(), "1:\n3.68\n3.28\n3.59\n0.56\n")

    def test_eval_2(self):
        r = StringIO("10:\n1952305\n1531863")
        w = StringIO()
        netflix_eval(r, w)
        self.assertEqual(
            w.getvalue(), "10:\n2.88\n2.63\n0.27\n")

    def test_eval_3(self):
        r = StringIO("10010:\n1462925\n52050\n650466")
        w = StringIO()
        netflix_eval(r, w)
        self.assertEqual(
            w.getvalue(), "10010:\n2.2\n1.99\n2.04\n1.33\n")

    def test_eval_4(self):
        r = StringIO("7636:\n1512279\n1105843\n304068")
        w = StringIO()
        netflix_eval(r, w)
        self.assertEqual(
            w.getvalue(), "7636:\n4.35\n3.36\n3.78\n0.82\n")


    # def test_eval_2(self):
    #     r = StringIO("1:\n1046323\n1080030\n1830096\n")
    #     w = StringIO()
    #     netflix_eval(r, w)
    #     self.assertEqual(
    #         w.getvalue(), "1:\n3\n3\n3\n0.90\n")

    # def test_eval_3(self):
    #     r = StringIO("10040:\n2417853\n1207062\n2487973\n")
    #     w = StringIO()
    #     netflix_eval(r, w)
    #     self.assertEqual(
    #         w.getvalue(), "10040:\n2.4\n2.4\n2.4\n0.90\n")

# ----
# main
# ----			
if __name__ == '__main__':
    main()

""" #pragma: no cover
% coverage3 run --branch TestNetflix.py >  TestNetflix.out 2>&1



% coverage3 report -m                   >> TestNetflix.out



% cat TestNetflix.out
.
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK
Name             Stmts   Miss Branch BrPart  Cover   Missing
------------------------------------------------------------
Netflix.py          27      0      4      0   100%
TestNetflix.py      13      0      0      0   100%
------------------------------------------------------------
TOTAL               40      0      4      0   100%

"""
