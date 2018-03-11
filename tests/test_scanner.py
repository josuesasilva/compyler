import unittest
from scanner.scanner import Scanner
from scanner.token import TokenEnum

class TestScanner(unittest.TestCase):

    def setUp(self):
        self.file = open('tests/program.po', 'r')
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
        

    def test_eof(self):
        while not self.scanner.is_eof():
            self.scanner.get()
        self.assertTrue(self.scanner.is_eof())

    def test_scan(self):
        tokens = self.scanner.scan()
        self.assertEqual(len(tokens[TokenEnum.TYPE]), 3)
        self.assertEqual(len(tokens[TokenEnum.INTEGER]), 3)
        self.assertEqual(len(tokens[TokenEnum.COLON]), 3)
        self.assertEqual(len(tokens[TokenEnum.COMMA]), 1)
        self.assertEqual(len(tokens[TokenEnum.IDENTIFIER]), 9)
        self.assertEqual(len(tokens[TokenEnum.SEMICOLON]), 8)
        self.assertEqual(len(tokens[TokenEnum.ASSIGNMENT]), 3)
        self.assertEqual(len(tokens[TokenEnum.KEYWORD]), 2)
