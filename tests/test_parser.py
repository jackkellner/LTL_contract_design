import os, sys, unittest
sys.path.append(os.path.join(os.getcwd(), os.path.pardir))
from src.parser import Parser
from src.check import Checks
from src.check import Check

class TestParser(unittest.TestCase):

    def test_parser(self):
        parser_obj = Parser()
        parser_obj.parse('./tests/waiter_customer.txt')

    def test_checks(self):
    	checks = Checks()
    	checks.run()





