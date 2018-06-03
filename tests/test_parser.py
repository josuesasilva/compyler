import unittest
from scanner.scanner import Scanner
from scanner.token import TokenEnum
from parser.ll_1 import LL1

class TestParser(unittest.TestCase):

    def setUp(self):
        self.file = open('tests/program.po', 'r')
        self.scanner = Scanner(self.file)
        self.scanner.scan()
        self.tokens = self.scanner.tokens_list
        self.parser = LL1(self.tokens)

    def tearDown(self):
        self.file.close()

    def test_eoftoken(self):
        self.assertEqual(self.tokens[-1].token, TokenEnum.EOF)

    def test_keywords(self):
        self.assertEqual(len(self.parser.keywords), 8)

    def test_index(self):
        self.assertEqual(self.parser.index, 0)

    
