PYTTHON=python3

test:
	make test_scanner
	make test_parser

test_scanner:
	$(PYTTHON) -m unittest tests/test_scanner.py -v

test_parser:
	$(PYTTHON) -m unittest tests/test_parser.py -v
