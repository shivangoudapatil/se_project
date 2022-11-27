from getplag import getplag

txt1 = ""
txt2 = "int = 5"
txt3 = ""

import unittest

tc = unittest.TestCase()

print(getplag(txt1,txt2))
print(getplag(txt1,txt3))
print(getplag(txt2,txt2))

tc.assertTrue(0<=getplag(txt1,txt2)<=1)
tc.assertTrue(0<=getplag(txt1,txt3)<=1)
tc.assertTrue(0<=getplag(txt2,txt2)<=1)