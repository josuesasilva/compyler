PYTTHON=python

test:
	make test_scanner

test_scanner:
	$(PYTTHON) -m unittest tests/test_scanner.py -v
