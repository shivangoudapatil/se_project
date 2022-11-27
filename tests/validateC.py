import os

def validateProgramType(fileName):
    ext = os.path.splitext(fileName)[-1].lower()
    if(ext==".c"):
        #print("Valid File Type")
        return True
    else:
        #print("Not a valid file type")
        return False


import unittest

tc = unittest.TestCase()

tc.assertEqual(validateProgramType("hello.c"),True)
tc.assertEqual(validateProgramType("prog1.c"),True)
tc.assertFalse(validateProgramType("hi.cpp"),False)
tc.assertFalse(validateProgramType("prog2c.py"),False)