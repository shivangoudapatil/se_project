from comment_strip import comment_strip

import unittest

tc = unittest.TestCase()

#print(comment_strip("//hi"))

tc.assertEqual(comment_strip("//hi"),"")
tc.assertEqual(comment_strip("int x = 5;// declaring x"),"int x = 5;")
