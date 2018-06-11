import unittest
from scanner.scanner import Scanner
from scanner.token import TokenEnum

class TestScanner(unittest.TestCase):

    def setUp(self):
        self.file = open('tests/program-old.po', 'r')
        self.scanner = Scanner(self.file)

    def tearDown(self):
        self.file.close()

    def test_get(self):
        self.assertEqual(self.scanner.get(), 'I')
        self.scanner.peek()
        self.assertEqual(self.scanner.get(), 'N')
        self.assertEqual(self.scanner.get(), 'T')
        self.assertEqual(self.scanner.get(), 'E')
        self.assertEqual(self.scanner.get(), 'I')
        self.scanner.peek()
        self.assertEqual(self.scanner.get(), 'R')
        self.assertEqual(self.scanner.get(), 'O')

    def test_peek(self):
        self.assertEqual(self.scanner.peek(), 'I')
        self.assertEqual(self.scanner.peek(), 'I')
        self.assertEqual(self.scanner.peek(), 'I')
        self.scanner.get()
        self.assertEqual(self.scanner.peek(), 'N')
        self.assertEqual(self.scanner.peek(), 'N')

    def test_getline(self):
        self.assertEqual(self.scanner.get_line(), 'INTEIRO: numero1;\n')
        self.assertEqual(self.scanner.get_line(), '\n')

    def test_peekline(self):
        self.assertEqual(self.scanner.peek_line(), 'INTEIRO: numero1;\n')
        self.assertEqual(self.scanner.peek_line(), 'INTEIRO: numero1;\n')

    def test_islinecomment(self):
        self.assertEqual(self.scanner.is_linecomment(), False)

    def test_eof(self):
        while not self.scanner.is_eof():
            self.scanner.get()
        self.assertTrue(self.scanner.is_eof())

    def test_scan(self):
        tokens = self.scanner.scan()
        self.assertEqual(len(tokens[TokenEnum.TYPE]), 4)
        self.assertEqual(len(tokens[TokenEnum.INTEGER]), 5)
        self.assertEqual(len(tokens[TokenEnum.COLON]), 4)
        self.assertEqual(len(tokens[TokenEnum.COMMA]), 1)
        self.assertEqual(len(tokens[TokenEnum.IDENTIFIER]), 15)
        self.assertEqual(len(tokens[TokenEnum.SEMICOLON]), 9)
        self.assertEqual(len(tokens[TokenEnum.ASSIGNMENT]), 6)
        self.assertEqual(len(tokens[TokenEnum.KEYWORD]), 3)
        self.assertEqual(len(tokens[TokenEnum.TEXT]), 1)
        self.assertEqual(len(tokens[TokenEnum.FLOAT]), 1)
        self.assertEqual(len(tokens[TokenEnum.ARITHMETIC]), 2)

    def test_token_list(self):
        self.scanner.scan()
        self.assertEqual(len(self.scanner.tokens_list), 51)
